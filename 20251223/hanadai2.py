#花屋の支払金額を求める
#値段
rose_v=500 #バラの単価
sun_v=400 #ひまわりの単価
tulip_v=700 #チューリップの単価
#個数
rose_c=18 #個数
sun_c=8-2
tulip_c=21-5
#割引率
rate=1-0.1

#計算
sum_v=(rose_v*rose_c)+(sun_v*sun_c)+(tulip_v*tulip_c)
payment=sum_v*rate

print(payment)

#結果を表示
print("買い物お合計は",sum＿v,"円")
print("割引してもらうと",payment,"円")
      
