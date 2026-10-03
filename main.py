import datetime
import os

def log_conversation(user_msg, bot_msg):
    """Conversation history ko text file mein log karta hai"""
    with open("chat_history.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] User: {user_msg}\n")
        f.write(f"[{timestamp}] Bot: {bot_msg}\n\n")

def get_bot_response(user_input):
    text = user_input.lower().strip()
    
    # 1. Greetings (Intents)
    if any(word in text for word in ["hi", "hello", "hey", "salam"]):
        return "Hello! Main Syntecxhub ka AI chatbot hoon. Main aapki kya madad kar sakta hoon?"
    
    elif any(word in text for word in ["how are you", "kese ho", "kaise ho"]):
        return "Main bilkul theek hoon! Aap batayein, aap kaise hain aur aaj kya seekhna chahte hain?"
    
    # 2. Small Talk
    elif "your name" in text or "naam ki bat hai" in text:
        return "Mera naam Syntecxhub AI Assistant hai."
    
    elif "bye" in text or "exit" in text or "allah hafiz" in text:
        return "Allah Hafiz! Phir milte hain. Apna khayal rakhiyega."
        
    # 3. Help Intent
    elif "help" in text or "madad" in text:
        return "Main aapko greetings, small talk aur AI/Syntecxhub se mutaliq sawalon ke jawab dene mein madad kar sakta hoon."
        
    # 4. Domain Knowledge Base (AI & Syntecxhub info)
    elif "syntecxhub" in text:
        return "Syntecxhub ek aisi platform hai jo students ko Web Development, AI, aur Data Science jese fields mein practical internships aur real-world projects faraham karti hai."
        
    elif "artificial intelligence" in text or "ai" in text:
        return "Artificial Intelligence (AI) computer science ki wo branch hai jo aisi machines banati hai jo insano ki tarah soch sakein aur faisle kar sakein."
    
    elif "chatbot" in text:
        return "Chatbot ek software application hai jo text ya voice ke zariye insani baat-cheet (conversation) ko simulate karti hai."
        
    # Default response if no pattern matches
    else:
        return "Maaf kijiye ga, main aapki yeh baat samajh nahi saka. Aap 'help' type karke dekh sakte hain ke main kya Jawab de sakta hoon."

def main():
    print("==========================================")
    print("   SYNTECXHUB - RULE-BASED CHATBOT (AI)   ")
    print("==========================================\n")
    print("Bot: Hello! Baat karne ke liye kuch type karein. (Chat khatam karne ke liye 'bye' ya 'exit' likhein)\n")
    
    while True:
        user_input = input("Aap: ")
        
        if not user_input.strip():
            continue
            
        # Get response from rules
        response = get_bot_response(user_input)
        print(f"Bot: {response}\n")
        
        # Log conversation to file
        log_conversation(user_input, response)
        
        if user_input.lower().strip() in ["bye", "exit", "allah hafiz"]:
            break

if __name__ == "__main__":
    main()