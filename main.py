import StoreSQL

# 함수 호출 예시
busan_df = StoreSQL.search_store_by_region("부산", "dong_NM", "반여2동")
gangwon_df = StoreSQL.search_store_by_region("강원", "dong_NM", "무실동")

print(busan_df)
print(gangwon_df)
