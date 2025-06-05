def process_plan_image(image_bytes):
    # ✅ تحليل مخطط تجريبي
    # يمكن ربطه لاحقًا بـ Grounded SAM أو YOLOv8 للكشف الذكي
    rooms = ["Living Room", "Bedroom", "Kitchen", "Dining Room"]
    output = {}
    for room in rooms:
        output[room] = {
            "suggested_items": ["كنبة", "سرير", "طاولة"],
            "dimensions": "approx. 4x5m"
        }
    return output
