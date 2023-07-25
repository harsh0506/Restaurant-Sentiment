import random
import time 
def generate_review():
    rating = random.randint(1, 5)
    food = random.choice(["pizza", "pasta", "burger", "salad", "steak", "chicken", "fish", "dessert", "drink"])
    ambience = random.choice(["nice", "bland", "noisy", "crowded", "romantic", "casual", "classy", "homey", "sterile"])
    hygiene = random.choice(["clean", "dirty", "well-maintained", "run-down", "sanitary", "unsanitary", "disgusting", "spotless", "filthy"])
    service = random.choice(["excellent", "good", "bad", "terrible", "slow", "fast", "friendly", "rude", "inattentive"])
    review = f"The {food} was delicious! The ambience was {ambience}, the hygiene was {hygiene}, and the service was {service}. The rating was {rating} out of 5 stars."
    return review

def main():
    start_time = time.time()
    reviews = []
    for i in range(500):
        review = generate_review()
        reviews.append(review)

    print(reviews[0])
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.6f} seconds")

if __name__ == "__main__":
    main()