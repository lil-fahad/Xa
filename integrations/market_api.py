def search_marketplace(item_name: str):
    query = item_name.replace(" ", "+")
    return {
        "alibaba": f"https://www.alibaba.com/trade/search?SearchText={query}",
        "amazon": f"https://www.amazon.com/s?k={query}",
        "wayfair": f"https://www.wayfair.com/keyword.php?keyword={query}",
        "ikea": f"https://www.ikea.com/sa/en/search/products/?q={query}",
        "noon": f"https://www.noon.com/saudi-en/search?q={query}"
    }
