def solution(s):
    new_format = s
    # Define a dictionary to map old format specifiers to new placeholders
    format_map = {
        "%d": "{}",  # Integer
        "%f": ".{}",  # Float (assuming at least one digit after decimal)
        "%s": "{}",  # String
    }

    seen = set()  # Track seen format specifier types

    # Iterate over characters and replace format specifiers with placeholders
    for i, char in enumerate(s):
        if char == '%' and (i == 0 or s[i - 1] != '%'):
            # Handle consecutive percent signs (%%) as a literal percent sign
            if i + 1 < len(s) and s[i + 1] == '%':
                new_format = new_format[:i] + '%' + new_format[i + 2:]
            else:
                # Handle single percent sign (%) as a literal percent sign
                new_format = new_format[:i] + '%' + new_format[i + 1:]
        elif char in format_map and char not in seen:
            # Replace non-escaped format specifiers (except consecutive %%)
            new_format = new_format[:i] + format_map[char] + new_format[i + 1:]
            seen.add(char)  # Mark format specifier type as seen

    print(new_format)
    return new_format

s="We expect the %f%% growth this week"
solution(s)