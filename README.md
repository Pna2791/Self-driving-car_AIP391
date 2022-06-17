# Self-driving-car_AIP391
## AI subject project

**Authors**: Anh Phan Ngoc, Thinh Ngo Duy, Truong Nguyen Nhat


**Proposal**: [Here](https://docs.google.com/document/d/1pJ-1mpVCfOzMSC11danirGs2GOsCmb-buNbJHjdytLo/edit?usp=sharing) |
**Timelines**: [Here](https://docs.google.com/spreadsheets/d/1tI2cD12YLB2aPiFoT3_adGZfaXKjOTtR2en1cJyj28g/edit?usp=sharing) | 
**Google Drive folder**: [Here](https://drive.google.com/drive/folders/14z2X1SkVipk8dSuBQIf7gDxpjtQ_vyRX?usp=sharing)


# [Timeline](https://docs.google.com/spreadsheets/d/1tI2cD12YLB2aPiFoT3_adGZfaXKjOTtR2en1cJyj28g/edit?usp=sharing)

![image](https://user-images.githubusercontent.com/105489258/169793574-2324b618-0e06-4782-bb65-7392558cce07.png)


# [Flow chart](https://app.diagrams.net/#G1B7SDmvY0hIDqaHdsrO-5gehTCWmqGAVJ)
<p align="center">
  <img src="https://user-images.githubusercontent.com/87382851/169862843-df417c02-97ff-485f-8590-8b3e131b3d97.png">
</p>


# Problems
1. **Về điều dạy cho xe học:**
- Không thực hiện training cho xe trong môi trường ảo với Deep Q Neural, Double Deep Q Neural hoặc NEAT (Neuroevolution of augmenting topologies). Hiện tại thì NEAT tham khảo qua các dự án dùng NEAT thì thấy thuật toán đó cho kết quả tốt hơn nhưng nhóm chưa có khả năng implementation lại cấu trúc đó.
- Hiện tại nhóm đang hướng đến phương pháp học các lệnh trên việc điều khiển thực tế. Với phương pháp này nhóm sợ không đủ dữ liệu để cho model học.
2. **Về nhận dạng các biển báo:** hiện tại để đạt được 10-15fps thì nhóm đang chỉ nhận dạng các biển báo chính như giới hạn tốc độ 40, 60, 70, 90; biển hết cấm 40, 60, 70 và bộ 3 đèn giao thông, biến stop.
3. **Về nhận diện lane:** để đơn giản hóa cho khả năng mô phỏng thì nhóm đang đang chỉ làm về nhận dạng đường có 1 làn đường 1 chiều (chỉ có 2 line liền 2 bên thôi). Nếu có thể thì nhóm sẽ phát triển thêm 1 mô hình đường 2-3 lane, đường rẽ nhánh.
