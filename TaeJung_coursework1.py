# 1. 재고 딕셔너리 (비어 있는 상태로 시작)
inventory = {}

# 2. 샘플 아이템 데이터 (이름: str, 수량: int, 가격: float)
sample_item_1 = {
    "name": "Laptop",
    "quantity": 5,
    "price": 799.99
}

sample_item_2 = {
    "name": "Chair",
    "quantity": 10,
    "price": 49.50
}

# 3. 샘플 아이템을 inventory에 넣기
# 여기서는 간단히 숫자 ID를 key로 사용
inventory[101] = sample_item_1
inventory[102] = sample_item_2

# (선택) 나중에 쓸 카테고리 리스트와 ID 셋
categories = ["Electronics", "Home", "Office"]
product_ids = {101, 102}

# 확인용 출력
print(inventory)
