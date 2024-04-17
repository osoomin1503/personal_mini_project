## keras와 pytorch로 MNIST 데이터를 분류하는 모델 개발
(1) Keras
    - TensorFlow 및 Theano와 같은 백엔드 엔진 위에 구축
    - Sequential 모델을 사용하여 간단하게 모델을 층별로 쌓을 수 있음.
    - 모델의 각 레이어는 Sequential 모델의 add() 메서드를 사용하여 쉽게 추가됨.
(2) PyTorch
    - 동적 계산 그래프를 사용
    - nn.Module 클래스를 상속하여 정의되며, forward() 메서드를 재정의하여 데이터가 모델을 통과하는 방법을 지정
    - 사용자가 직접 레이어를 구성하고 커스터마이징할 수 있음
