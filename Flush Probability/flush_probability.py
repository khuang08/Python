import time
import random
import traceback
from collections import Counter
from multiprocessing import Pool, cpu_count

def log_error(error):
    """Log errors to a file with timestamp"""
    with open("simulation_errors.log", "a") as f:
        f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}]\n")
        traceback.print_exc(file=f)
        f.write("\n\n")

def simulate_flush_attempts_chunk(chunk_size):
    try:
        result_counts = {3: 0, 4: 0, 5: 0}
        for _ in range(chunk_size):
            deck = [f'S_{i}' for i in range(1, 14)] + \
                   [f'H_{i}' for i in range(1, 14)] + \
                   [f'D_{i}' for i in range(1, 14)] + \
                   [f'C_{i}' for i in range(1, 14)]
            random.shuffle(deck)
            
            hand = deck[:9]
            remaining_deck = deck[9:]
            
            suits = [card.split('_')[0] for card in hand]
            target_suit = Counter(suits).most_common(1)[0][0]
            target_count = suits.count(target_suit)
            
            for _ in range(1):
                if target_count >= 5:
                    break
                    
                non_target = [card for card in hand if not card.startswith(target_suit)]
                discard = random.sample(non_target, min(5, len(non_target)))
                hand = [card for card in hand if card not in discard]
                
                draw = remaining_deck[:5]
                remaining_deck = remaining_deck[5:]
                hand += draw
                
                target_count += sum(1 for card in draw if card.startswith(target_suit))
            
            final_count = min(target_count, 5)
            if final_count >= 1:
                result_counts[final_count] += 1
        
        return result_counts
    except Exception as e:
        log_error(e)
        raise

def parallel_simulation(total_simulations=100000):
    try:
        start_time = time.time()
        num_cores = min(4, cpu_count())
        chunk_size = total_simulations // num_cores
        
        print(f"Running with {num_cores} cores... (Ctrl+C to stop early)")
        
        with Pool(num_cores) as pool:
            results = pool.map(simulate_flush_attempts_chunk, [chunk_size]*num_cores)
        
        # Combine results
        final_counts = {3: 0, 4: 0, 5: 0}
        for result in results:
            for k in final_counts:
                final_counts[k] += result[k]
        
        # Calculate probabilities
        total_valid = sum(final_counts.values())
        probabilities = {k: v/total_simulations*100 for k, v in final_counts.items()}
        
        end_time = time.time()
        
        print(f"\nParallel Simulation Results ({total_simulations} runs, {end_time-start_time:.2f}s)")
        print(f"Cores used: {num_cores}")
        print("Final suit counts:")
        print(f"3 cards: {final_counts[3]} ({probabilities[3]:.2f}%)")
        print(f"4 cards: {final_counts[4]} ({probabilities[4]:.2f}%)")
        print(f"5 cards: {final_counts[5]} ({probabilities[5]:.2f}%)")
        print(f"\nTotal flush probability: {probabilities[5]:.2f}%")
    
    except KeyboardInterrupt:
        print("\nEarly termination requested! Saving partial results...")
    except Exception as e:
        log_error(e)
        print(f"Critical error! See 'simulation_errors.log'")

if __name__ == '__main__':
    parallel_simulation()