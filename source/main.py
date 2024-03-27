import random

from fibonacci_sequence import recursive_fibonacci_sequence, iterative_fibonacci
from searching_number import searching_inlist_first_variant, searching_inlist_second_variant, generate_unique_numbers
from word_occurrences import count_word_first_variant, count_word_second_variant, file_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from time import perf_counter

pdfFile = PdfPages("results_file.pdf")


def show_results_for_fibonacci(variant, fibonacci_input):
    fibonacci_output = []
    for num in fibonacci_input:
        start = perf_counter()
        result = variant(num)
        end = perf_counter()
        total_time = end - start
        fibonacci_output.append(total_time)
    plt.plot(fibonacci_input, fibonacci_output)
    plt.title(f"Measure time for fibonacci inputs using {variant.__name__}")
    plt.xlabel("Inputs")
    plt.ylabel("Time(seconds)")
    plt.grid(True)
    pdfFile.savefig()
    plt.show()
    plt.close()
    print(fibonacci_output)


def show_results_for_searching_number(variant, input_list_of_lists, search_num):
    inputs = [10, 100, 1000, 10000]
    searching_runtime = []
    for sublist in input_list_of_lists:
        start = perf_counter()
        result = variant(sublist, search_num)
        end = perf_counter()
        total_time = end - start
        searching_runtime.append(total_time)
    plt.title(f"Measure time for searching number from list using {variant.__name__}")
    plt.plot(inputs, searching_runtime, marker='o')
    plt.scatter(inputs, searching_runtime, color='red')
    plt.xlabel("List Length")
    plt.ylabel("Time(seconds)")
    plt.grid(True)
    pdfFile.savefig()
    plt.show()
    plt.close()


def show_results_for_word_occurrences(variant, list_of_data, the_word):
    inputs = [10, 100, 1000, 10000]
    input_runtime = []
    for data in list_of_data:
        start = perf_counter()
        result = variant(data, the_word)
        end = perf_counter()
        total_time = end - start
        input_runtime.append(total_time)
    plt.title(f"Measure time for word_occurrences from text using {variant.__name__}")
    plt.plot(inputs, input_runtime, marker='o')
    plt.scatter(inputs, input_runtime, color='red')
    plt.xlabel("Text Length")
    plt.ylabel("Time(seconds)")
    plt.grid(True)
    pdfFile.savefig()
    plt.show()
    plt.close()


def main():
    fibonacci_input = [5, 10, 15, 20, 25, 30, 35, 40]
    fibonacci_variants = [recursive_fibonacci_sequence, iterative_fibonacci]

    # Call the function to show results and save to the same PDF file
    for variant in fibonacci_variants:
        show_results_for_fibonacci(variant, fibonacci_input)

    list_of_searching_lists = []
    for num in [10, 100, 1000, 10000]:
        numbers = generate_unique_numbers(num)
        list_of_searching_lists.append(numbers)
    merge_list = [item for sublist in list_of_searching_lists for item in sublist]
    searching_numbers_variants = [searching_inlist_first_variant, searching_inlist_second_variant]
    for variant in searching_numbers_variants:
        show_results_for_searching_number(variant, list_of_searching_lists,
                                          random.choice(merge_list))

    list_of_texts = []
    text10 = file_data("text_10_words.txt")
    text100 = file_data("text_100_words.txt")
    text1000 = file_data("text_1000_words.txt")
    text10000 = file_data("text_10000_words.txt")
    list_of_texts.extend([text10, text100, text1000, text10000])
    word_occurrences_variants = [count_word_first_variant, count_word_second_variant]
    for variant in word_occurrences_variants:
        show_results_for_word_occurrences(variant, list_of_texts, "with")

    # Close the PDF file after saving all plots
    pdfFile.close()


if __name__ == "__main__":
    main()
