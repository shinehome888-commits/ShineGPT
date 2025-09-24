# generate_lessons.py
import gzip

# Base topics for scalability
topics = [
    "The 4th Industrial Revolution",
    "Artificial Intelligence (AI)",
    "Blockchain",
    "Cryptocurrency",
    "Web3",
    "Metaverse",
    "Big Data",
    "Cloud Computing",
    "IoT (Internet of Things)",
    "Digital Twins",
    "Smart Cities",
    "Cybersecurity",
    "Machine Learning",
    "NFTs",
    "DeFi",
    "DAOs",
    "Robotics",
    "Drones",
    "3D Printing",
    "AR & VR",
    "Future of Work"
]

# Generate 1500 lessons
with gzip.open("lessons.txt.gz", "wt", encoding="utf-8") as f:
    for i in range(1, 1501):
        topic = topics[(i - 1) % len(topics)]
        # Example: "Lesson 1: Introduction to The 4th Industrial Revolution"
        lesson_text = (
            f"{topic} – Lesson {i}: "
            f"This is part of the KS1 Empire Foundation's mission to teach digital literacy across Africa. "
            f"Stay curious. Stay empowered."
        )
        f.write(f"{i}|{lesson_text}\n")

print("✅ Generated 1,500 compressed lessons in 'lessons.txt.gz'")
