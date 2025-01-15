import pywhatkit as kit
import requests
import random

# A list of positive Bible verse references
bible_references = [
    "John 3:16", "Psalm 23:1", "Philippians 4:13", "Jeremiah 29:11", "Romans 8:28",
    "Isaiah 41:10", "Matthew 11:28", "Proverbs 3:5", "1 Corinthians 13:4", "Psalm 46:1",
    "Romans 6:23", "Romans 8:1", "Romans 10:9", "Matthew 28:19", "Genesis 1:1",
    "John 14:6", "Isaiah 40:31", "Psalm 34:8", "Ephesians 6:10", "2 Timothy 1:7",
    "John 10:10", "1 Peter 5:7", "Hebrews 11:1", "Psalm 121:1", "Matthew 6:33",
    "Luke 6:38", "Matthew 7:7", "Romans 5:8", "Proverbs 4:23", "Matthew 5:14",
    "Psalm 37:4", "James 1:5", "2 Corinthians 5:17", "Proverbs 22:6", "Hebrews 13:8",
    "Matthew 19:26", "Psalm 118:24", "Jeremiah 33:3", "Isaiah 55:8-9", "Colossians 3:23",
    "Psalm 139:14", "Romans 3:23", "Titus 2:11", "Mark 9:23", "Romans 12:2",
    "Galatians 5:22-23", "Isaiah 43:2", "Psalm 84:11", "Revelation 21:4", "John 15:13",
    "Romans 8:38-39", "Psalm 23:4", "1 John 1:9", "2 Corinthians 12:9", "Luke 1:37",
    "1 John 4:19", "Ephesians 2:8-9", "Psalm 51:10", "Isaiah 53:5", "John 8:32",
    "Matthew 5:3", "Philippians 4:6-7", "Psalm 16:11", "1 Thessalonians 5:16-18",
    "Isaiah 26:3", "Proverbs 3:6", "Revelation 3:20", "Matthew 7:24-25", "Romans 15:13",
    "John 6:35", "Matthew 4:4", "1 Peter 2:24", "Isaiah 55:12", "Matthew 28:20",
    "Matthew 6:9-13", "Romans 10:17", "Philippians 1:6", "John 14:27", "James 1:2-4",
    "Luke 12:31", "Luke 4:18", "Psalm 27:1", "2 Corinthians 9:8", "James 4:7-8",
    "Matthew 11:29", "Proverbs 18:10", "Romans 15:5-6", "Romans 13:10", "John 3:3",
    "Romans 8:18", "Matthew 9:37-38", "2 Corinthians 5:21", "Proverbs 3:12", "2 Samuel 22:31",
    "Isaiah 40:29", "Isaiah 61:1", "John 8:36", "Proverbs 4:9", "Proverbs 15:1",
    "2 Timothy 4:7", "Romans 15:1", "Psalm 143:8", "Romans 8:32", "Luke 1:50", "Romans 2:7",
    "Matthew 19:14", "Psalm 20:4", "Mark 10:27", "Galatians 2:20", "Romans 4:20-21",
    "Isaiah 41:13", "2 Corinthians 1:3-4", "Romans 5:1-2", "Matthew 7:12", "Psalm 32:8",
    "Romans 5:5", "Matthew 9:29", "John 1:12", "Matthew 18:19-20", "Isaiah 40:28-31",
    "Romans 8:24-25", "John 14:1-2", "Romans 5:10", "John 7:37-38", "Psalm 119:105",
    "Romans 6:4", "1 Corinthians 9:24", "Luke 15:10", "Psalm 34:18", "Matthew 5:10",
    "James 5:16", "Matthew 4:19", "Psalm 56:3", "2 Corinthians 4:16-18", "John 13:34-35",
    "Romans 3:24", "1 John 4:8", "Psalm 118:8", "John 17:17", "Psalm 9:9-10", "Romans 12:9-10",
    "Psalm 62:1-2", "Matthew 28:18-20", "Philippians 4:13", "Hebrews 10:23", "Psalm 35:9-10",
    "Romans 1:16", "Colossians 2:6-7", "Isaiah 40:31", "2 Samuel 22:4", "Psalm 61:3", "Romans 4:5",
    "Matthew 6:34", "Psalm 90:17", "Hebrews 10:24", "Psalm 46:10", "Matthew 10:16", "John 16:33",
    "Psalm 139:23-24", "Romans 8:5", "Isaiah 41:10", "Romans 8:7", "Philippians 4:4", "2 Samuel 22:31",
    "Psalm 19:14", "Psalm 25:4", "Psalm 27:14", "Isaiah 55:6", "Matthew 7:13", "Romans 12:12",
    "Romans 6:14", "John 1:1-2", "Isaiah 53:6", "Psalm 33:18", "Romans 8:28-30", "Matthew 28:16-17",
    "Romans 15:13", "Philippians 1:6", "2 Thessalonians 2:16-17", "Psalm 18:2", "2 Corinthians 12:9",
    "Romans 8:35-39", "1 John 5:14-15", "Romans 12:9", "Psalm 34:17", "Psalm 23:6", "Ephesians 3:20",
    "Galatians 6:9", "Isaiah 55:10-11", "Hebrews 4:16", "Romans 8:31", "Psalm 91:1-2", "Romans 5:20-21",
    "Matthew 5:14", "John 15:5", "2 Corinthians 1:3", "Romans 8:28", "Romans 6:23", "Psalm 119:105",
    "Matthew 6:25-34", "Philippians 4:19", "John 14:27", "2 Corinthians 5:17", "Psalm 23:5", "Proverbs 31:25",
    "Isaiah 55:12", "Psalm 46:1", "Matthew 5:14-16", "Romans 6:23", "John 8:32", "Psalm 119:11", "Isaiah 40:31",
    "John 10:10", "Romans 5:8", "Psalm 34:18", "Luke 12:31", "Psalm 18:24", "Psalm 147:3", "Isaiah 43:1",
    "Matthew 5:9", "Romans 8:16", "Psalm 103:1-5", "John 16:33", "Psalm 51:10", "Hebrews 13:5", "Romans 15:13",
    "Isaiah 26:3", "Psalm 118:24", "Psalm 100:5", "Isaiah 41:13", "John 7:37-38", "Psalm 61:3", "Matthew 19:26",
    "Isaiah 41:10", "Psalm 103:11", "Romans 8:1", "Romans 8:38-39", "Psalm 139:13-14", "Romans 5:5",
    "Matthew 11:28-30", "Psalm 25:4-5", "Romans 12:12", "Isaiah 58:11", "2 Corinthians 9:8", "Ephesians 3:16-19",
    "Psalm 147:5", "Luke 1:37", "Philippians 4:13", "Isaiah 53:4-5", "Psalm 28:7", "Romans 5:1", "Matthew 28:19-20",
    "John 16:33", "Romans 6:11", "Psalm 119:23-24", "Psalm 91:4", "Jeremiah 29:11", "Romans 8:24-25",
    "Ephesians 2:10", "Philippians 4:7", "Luke 1:50", "Isaiah 61:3", "Romans 15:13", "Matthew 11:29-30", 
    "Isaiah 61:10", "Psalm 71:14", "Romans 5:8", "Ephesians 6:10-11", "Hebrews 10:23", "Psalm 34:4", 
    "Romans 12:2", "Matthew 5:14", "Psalm 18:1", "John 1:12", "1 Peter 5:10", "Romans 8:24", "Isaiah 12:2"
]

# Function to get random Bible verses from the API
def get_random_bible_verses(count=3):
    # Select random verses from the list of references
    selected_verses = random.sample(bible_references, count)
    
    verses = []
    
    # Fetch each verse from the API
    for reference in selected_verses:
        url = f"https://bible-api.com/{reference}"
        response = requests.get(url, verify=False)  # Disable SSL verification (Not recommended for production)
        
        # Check if the response is successful
        if response.status_code == 200:
            verse_data = response.json()
            verse_text = verse_data['text']
            verses.append(f"{verse_text} ({reference})")
        else:
            print(f"Error fetching verse {reference}: {response.status_code}")
    
    return verses

# Function to send WhatsApp messages using pywhatkit
def send_whatsapp_message(phone_number, message):
    # Send message using pywhatkit
    kit.sendwhatmsg_instantly(phone_number, message)
    print(f"Message sent: {message}")

# Main function
def main():
    # Get random Bible verses
    verses = get_random_bible_verses(count=3)
    if not verses:
        print("Failed to fetch Bible verses.")
        return

    # Join the verses into a single message
    message_body = "\n\n".join(verses)

    # WhatsApp recipient's phone number (in the format: 'whatsapp:+1234567890')
    phone_number = 'whatsapp:+1234567890'  # Replace with your recipient's WhatsApp number

    # Send the message immediately
    send_whatsapp_message(phone_number, message_body)

if __name__ == '__main__':
    main()
