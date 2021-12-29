def count_substring(string, sub_string):
    count=0
    for c in range(len(string)):
        if string[c:].startswith(sub_string):
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
