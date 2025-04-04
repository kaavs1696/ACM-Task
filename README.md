# Grover's Algorithm

## Introduction

Imagine a massive collection of unsorted and unfiltered data, and from that, we need to find something useful. For example, if there are a thousand boxes in front of you, but only one of them contains a surprise gift, it would be extremely tedious and time-consuming to open each box one by one to find the right one.

A classical computer would solve this problem sequentially, checking each item one at a time. However, quantum computing offers a more efficient solution.

**Grover’s Algorithm** is a powerful quantum computing method that leverages the property of **superposition** to significantly speed up search and extraction processes. It can search through an **unsorted database of N items** and identify the correct item in approximately **√N steps**, drastically reducing computational effort and time.

Though Grover’s Algorithm has a simple function, its applications in quantum computing outperform classical methods in large-scale searches with massive datasets, making it a promising approach for the future of quantum computing.

---

## How It Works

My implementation of Grover’s Algorithm demonstrates its working with **two qubits**, meaning there are **four possible states**: **|00⟩, |01⟩, |10⟩, and |11⟩**. The goal is to search for the **|11⟩ state** efficiently.

### Steps in Grover’s Algorithm:

1. **Superposition**:

   - Initially, we ensure that all four possible states are in **equal quantum superposition**, allowing the system to explore all possibilities simultaneously.
   - This is achieved using **Hadamard gates**, which transform qubits into a superposition state.

2. **Oracle**:

   - A special quantum function called an **Oracle** is applied, marking the correct answer by flipping its phase using quantum logic gates whenever the required state is found.

3. **Amplification**:

   - The algorithm amplifies the probability of measuring the correct answer while reducing the probabilities of incorrect ones.
   - This is done using the **Grover Diffusion Operator (inversion about the mean)**, increasing the likelihood of selecting the correct state upon measurement.

4. **Measurement**:
   - Finally, when the system is measured, it collapses into its most probable state.
   - Due to the amplification step, the correct state is observed with a **high probability**.
   - Running the algorithm multiple times further increases the confidence in the correct result.

---

## Expected Results

On running this code, the state **|11⟩** should have the **highest probability measurement** since that is our required state. If the algorithm works correctly, **|11⟩ should be observed with maximum overall probability** as shown in the results.

---

## Applications

- **Database search**: Efficiently searching through large datasets.
- **Cryptanalysis**: Used in breaking cryptographic hash functions.
- **Optimization problems**: Finding optimal solutions in large solution spaces.
- **Pattern recognition**: Identifying patterns in machine learning and AI.

Grover’s Algorithm showcases the true potential of quantum computing, making it a revolutionary approach to solving complex problems more efficiently than classical methods.

## Steps to run the file (WINDOWS)

- Clone the repo:

```
git clone https://github.com/kaavs1696/ACM-Task.git
cd ACM-Task
```

- Install the required libraries to run the file

```
pip install -r requirements.txt
```

- Run the python file

```
python acm_task.py
```
