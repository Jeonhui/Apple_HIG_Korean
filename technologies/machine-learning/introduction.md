# **[technologies-machine-learning] introduction**

# Machine learning is a powerful and versatile tool that can help you improve existing experiences and create new ones that people love.
> 머신러닝은 기존 경험을 개선하고 사람들이 좋아하는 새로운 경험을 만들 수 있도록 도와줄 수 있는 강력하고 다목적인 도구이다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-machine-learning-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-machine-learning-intro_2x.png)

In addition to providing familiar features like image recognition and content recommendations, your app can use machine learning to forge deep connections with people and help them accomplish more with less effort.
> 이미지 인식 및 콘텐츠 추천과 같은 친숙한 기능을 제공할 뿐만 아니라, 당신의 앱은 머신 러닝을 사용하여 사람들과 깊은 관계를 구축하고 그들이 더 적은 노력으로 더 많은 것을 성취하도록 도울 수 있다.
>




Machine learning apps use *models* to perform tasks like recognizing images or finding relationships among numerical data. A great machine learning app depends on well-designed models as much as it depends on a well-designed UI and user experience. For insight into the process of designing models, see [Create ML](https://developer.apple.com/documentation/createml).
> 기계 학습 앱은 모델을 사용하여 이미지를 인식하거나 수치 데이터 간의 관계를 찾는 것과 같은 작업을 수행한다. 훌륭한 기계 학습 앱은 잘 설계된 UI와 사용자 경험에 의존하는 만큼 잘 설계된 모델에 의존한다. 모델 설계 프로세스에 대한 자세한 내용은 ML 작성을 참조하십시오.
>




As you design your models, consider the intended experience of your app so you can align your design decisions in both areas. It can take a long time to adjust the behavior of models and you should be prepared to change the way you use data and metrics if the app experience needs to change.
> 모델을 설계할 때는 앱의 의도된 경험을 고려하여 두 영역 모두에서 설계 결정을 조정할 수 있습니다. 모델의 동작을 조정하는 데 오랜 시간이 걸릴 수 있으며 앱 환경을 변경해야 할 경우 데이터 및 메트릭 사용 방식을 변경할 준비가 되어 있어야 합니다.
>




# **Designing the UI and user experience of a machine learning app**
> 머신러닝 앱의 UI 및 사용자 경험 설계
>




A machine learning app bases its behavior on the data it receives, and it reacts to changing information and conditions. This dynamic behavior makes designing the UI and user experience of a machine learning app uniquely challenging: instead of designing specific reactions to a static set of scenarios, you design it by teaching it how to interpret data and react accordingly.
> 머신러닝 앱은 수신하는 데이터를 기반으로 행동하며, 변화하는 정보와 조건에 반응한다. 이러한 동적 행동은 머신 러닝 앱의 UI 및 사용자 경험을 설계하는 것을 독특하게 어렵게 만든다. 정적 시나리오 세트에 대한 특정 반응을 설계하는 대신 데이터를 해석하고 그에 따라 반응하는 방법을 가르쳐서 설계한다.
>




To help you meet this challenge, consider the role that machine learning plays in your app. [Defining the role of machine learning in your app](../technologies/machine-learning/roles) describes several areas in which you can explore the ways machine learning can affect the experience your app provides.
> 이 문제를 해결하는 데 도움이 되도록 앱에서 기계 학습이 수행하는 역할을 고려하십시오. 앱에서 기계 학습의 역할을 정의하면 앱이 제공하는 경험에 영향을 미칠 수 있는 방법을 탐색할 수 있는 몇 가지 영역이 설명됩니다.
>




As you design your app’s UI and user experience, be guided by the role that machine learning plays in your app when considering ways to receive and display data. There are several patterns — grouped into *inputs* and *outputs* — that provide guidance in areas such as getting feedback, displaying data, handling mistakes, and enabling corrections. Use the guidance in these patterns to help you integrate machine learning into your app in ways that people appreciate.
> 앱의 UI와 사용자 경험을 설계할 때 데이터를 수신하고 표시하는 방법을 고려할 때 앱에서 기계 학습이 수행하는 역할에 따라 안내를 받습니다. 입력 및 출력으로 그룹화된 여러 패턴이 피드백 받기, 데이터 표시, 오류 처리 및 수정 활성화와 같은 영역에 대한 지침을 제공합니다. 이러한 패턴의 지침을 사용하여 사람들이 높이 평가하는 방식으로 기계 학습을 앱에 통합할 수 있습니다.
>



