# Simulation of RAG Knowledge Base
tiffin_knowledge = {
    "monday": "Paneer Butter Masala & 3 Rotis",
    "tuesday": "Dal Tadka, Rice & Salad",
    "price": "₹80 per meal"
}

def karvi_decision_engine(query):
    query = query.lower()
    
    # RAG Case: Just seeking information
    if "menu" in query or "price" in query:
        return "RAG Mode: Searching Database for menu/price info..."
    
    # MCP Case: Action needed (Something must happen)
    elif "cancel" in query or "book" in query or "order" in query:
        return "MCP Mode: Triggering Tool to update live order status..."
    
    else:
        return "Standard Chat: Just a general greeting."

print(karvi_decision_engine("I want to cancel my order for today"))