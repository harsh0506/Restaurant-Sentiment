import random
import time

def generate_name():
    first_name = random.choice(["John", "Mary", "Peter", "Jane", "David", "Elizabeth", "Michael", "Susan", "Christopher", "Jennifer"])
    last_name = random.choice(["Smith", "Jones", "Williams", "Brown", "Davis", "Wilson", "Taylor", "Thompson", "White", "Green"])
    return first_name + " " + last_name

def main():
    start_time = time.time()

    names = [generate_name() for _ in range(500)]
    
    end_time = time.time()

    print(names)
    print(f"Time taken: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()