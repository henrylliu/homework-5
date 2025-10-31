def mode(numbers):
    """Takes an input array and returns the mode
    
    Args:
        - numbers (array): An array of numbers. The numbers are not necessarily all integers

    Returns:
        - mode (int or float): The most commom element within the array
    """
    freqs = {}
    mode = None
    curr_freq = 0

    for num in numbers:
        freqs[num] = freqs.get(num, 0) + 1
        if freqs[num] > curr_freq:
            curr_freq = freqs[num]
            mode = num
            if curr_freq > (len(numbers) // 2):
                break
    return mode