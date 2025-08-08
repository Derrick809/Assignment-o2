# Standardize customer name
customer_name = "JANE DOE"
clean_name = customer_name.strip()
lowercase_name = clean_name.lower()
titlecase_name = clean_name.title()
print(f"clean name is {clean_name}")
print(f"Lowercase name is {lowercase_name}")
print(f"Titlecase name is {titlecase_name}")
# Format book titles
book_title = "the little prince"
formatted_title = book_title.capitalize()
print(f"book name is {formatted_title}")
#process a product code
product_code = "bk-457-nOVEL"
uppercase_code = product_code.upper()
print(f"the product is{uppercase_code}")
new_separator_code = product_code.replace("-", "/")
print(f"New product code is {new_separator_code}")
# count keyboards in a review
review = "This book is great. I love this book"
book_count = review.count("book")
print(book_count)
# check for digits in a serial number
serial_number = "987654321"
is_digit_only = serial_number.isdigit()
print(is_digit_only)
# create a new URL
url_parts = ["the", "book", "nook", "online"]
url_string = "-".join(url_parts)
sentence_string = " ".join(url_parts)
print(url_string)
print(sentence_string)
# Identify a Useer's input
offer_code = "FREESHIPPING"
is_offer_code_uppercase = offer_code.isupper()
print(is_offer_code_uppercase)
# Get the length of a string
feedback_message = "I am very happy with my order!"
message_length = len(feedback_message)
print(message_length)