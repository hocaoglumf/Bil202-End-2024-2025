def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
                # minimum elemanı kıyaslananla değiştir

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


#selection_sort([3,2,6,1])