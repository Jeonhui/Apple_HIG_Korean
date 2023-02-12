# **[technologies-siri] introduction**

# Siri makes it easy for people to accomplish everyday tasks quickly using voice, touch, or automation.
> Siri는 음성, 터치 또는 자동화를 사용하여 사람들이 일상적인 작업을 쉽게 수행할 수 있도록 합니다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Siri-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-Siri-intro_2x.png)

When you use [SiriKit](https://developer.apple.com/documentation/sirikit) to define the tasks and actions that your app supports, people can use Siri to perform them even when your app isn’t running. If you’re an accessory maker, you can also help people use Siri to control your accessories by integrating them with [HomeKit](../technologies/homekit/introduction/) or [AirPlay 2](../technologies/airplay/introduction/). Here are some of the ways people can use Siri to interact with your app or accessory:
> SiriKit을 사용하여 앱이 지원하는 작업과 작업을 정의하면 앱이 실행되지 않은 경우에도 사람들이 Siri를 사용하여 작업을 수행할 수 있습니다. 액세서리 제조업체인 경우 홈킷 또는 에어플레이 2와 통합하여 Siri를 사용하여 액세서리를 제어할 수도 있습니다. 다음은 사람들이 Siri를 사용하여 앱 또는 액세서리와 상호 작용할 수 있는 몇 가지 방법입니다:
>




- Ask Siri to perform a system-defined task that your app supports, like send a message, play a song, or start a workout.
- >  Siri에게 메시지 보내기, 노래 재생 또는 운동 시작과 같은 앱이 지원하는 시스템 정의 작업을 수행하도록 요청하십시오.

- Add a *shortcut*, which is a way to accelerate actions your app defines through onscreen interactions or by voice.
- >  화면 상호 작용 또는 음성으로 앱이 정의하는 작업을 가속화하는 방법인 바로 가기를 추가합니다.

- Use the Shortcuts app to adjust what a shortcut does, including combining several actions to perform one multistep shortcut.
- >  바로 가기 앱을 사용하여 여러 작업을 결합하여 하나의 다단계 바로 가기를 수행하는 것을 포함하여 바로 가기가 수행하는 작업을 조정할 수 있습니다.

- Tap a *suggestion* to perform a shortcut with your app (Siri can *suggest* shortcuts that people might want to perform, based on their current context and the information you provide).
- >  앱으로 바로 가기를 수행하려면 제안을 누릅니다(Siri는 현재 컨텍스트와 제공하는 정보를 기반으로 사람들이 수행하고 싶어할 수 있는 바로 가기를 제안할 수 있습니다).

- Use Siri to control an accessory that integrates with your app.
- >  Siri를 사용하여 앱과 통합되는 액세서리를 제어합니다.


![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/sirikit-intent-hero_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/sirikit-intent-hero_2x.png)

Siri works with your products on iPhone, iPad, Mac, Apple Watch, HomePod, and AirPods, so people can use it almost everywhere.
> Siri는 iPhone, iPad, Mac, Apple Watch, HomePod 및 에어팟에서 제품과 함께 작동하므로 사람들은 거의 모든 곳에서 사용할 수 있습니다.
>




When you make your app’s tasks available through Siri, you have several opportunities to customize the user experience. At a fundamental level, you customize the flow and functionality of the everyday tasks and actions you support to implement your business requirements. To reinforce this functionality throughout the user experience, you can write dialogue that reflects the style and tone of your company’s communications and design custom UI that incorporates your app’s visual style into the Siri interface.
> Siri를 통해 앱의 작업을 사용할 수 있게 하면 사용자 환경을 사용자 정의할 수 있는 몇 가지 기회가 있습니다. 기본적인 수준에서 비즈니스 요구사항을 구현하기 위해 지원하는 일상적인 작업과 작업의 흐름과 기능을 사용자 정의합니다. 사용자 경험 전반에 걸쳐 이 기능을 강화하기 위해 회사의 커뮤니케이션 스타일과 톤을 반영하는 대화를 작성하고 앱의 시각적 스타일을 Siri 인터페이스에 통합하는 사용자 지정 UI를 설계할 수 있습니다.
>




As you approach the job of integrating your app with Siri, assess the actions your app enables and learn how people use your app without voice interaction. Then consider the following steps:
> 앱을 Siri와 통합하는 작업에 접근함에 따라 앱이 가능하게 하는 작업을 평가하고 사람들이 음성 상호 작용 없이 앱을 사용하는 방법을 알아보십시오. 그런 다음 다음 단계를 고려하십시오:
>




- Identify key tasks in your app that people might want to perform on a regular basis.
- >  앱에서 사람들이 정기적으로 수행하고자 하는 주요 작업을 식별합니다.

- Drive engagement by telling the system about your app’s key tasks and by supporting suggestions.
- >  시스템에 앱의 주요 작업을 알리고 제안을 지원함으로써 참여를 유도합니다.

- For actions that people can perform through voice interaction, design functional conversational flows that feel natural.
- >  사람들이 음성 상호 작용을 통해 수행할 수 있는 작업의 경우, 자연스럽게 느껴지는 기능적 대화 흐름을 설계하십시오.

- Explore the various ways people might perform your app’s tasks — such as in a hands-free situation — and the devices they might be using, such as Apple Watch or iPad.
- >  핸즈프리 상황과 같이 사용자가 앱의 작업을 수행할 수 있는 다양한 방법과 Apple Watch 또는 iPad와 같은 사용자가 사용할 수 있는 장치를 살펴봅니다.


# **Identify your app’s key tasks**
> 앱의 주요 작업 식별
>




Tasks are at the core of your app’s integration with Siri. SiriKit builds on the idea of a person’s intention to perform a task by using the term *intent* to represent a task an app supports. The communication between your app and Siri is based on the intents — that is, the tasks — your app helps people perform.
> 작업은 당신의 앱과 시리의 통합의 핵심이다. SiriKit은 앱이 지원하는 작업을 나타내는 의도라는 용어를 사용하여 작업을 수행하려는 사람의 의도에 대한 아이디어를 기반으로 한다. 당신의 앱과 시리 사이의 의사소통은 당신의 앱이 사람들이 수행하는 것을 돕는 의도, 즉 작업을 기반으로 한다.
>




SiriKit defines *system intents* that represent common tasks — such as sending a message, calling a friend, and starting a workout — and groups related intents into domains. A *domain* is a category of tasks that Siri knows how to talk about, like messaging, calling, and workouts. For a complete list of domains and the actions in each domain that iOS and watchOS support, see [System intents](../technologies/siri/system-intents/).
> SiriKit은 메시지 보내기, 친구 호출, 운동 시작과 같은 일반적인 작업을 나타내는 시스템 의도를 정의하고 관련 의도를 도메인으로 그룹화합니다. 도메인은 메시지, 전화, 운동과 같이 시리가 대화할 줄 아는 작업의 범주입니다. 전체 도메인 목록 및 iOS 및 감시하는 각 도메인의 작업OS 지원은 시스템 의도를 참조하십시오.
>




When possible, take advantage of the intents that SiriKit defines. Using system-provided intents can make your job easier, while still giving you opportunities to customize the experience. However, if your app offers tasks that aren’t represented by system-defined intents — like ordering a meal or shopping for groceries — you can create a *custom intent* (for guidance, see [Custom intents](../technologies/siri/custom-intents/)).
> 가능하면 SiriKit이 정의하는 의도를 활용하십시오. 시스템에서 제공하는 의도를 사용하면 작업을 더 쉽게 수행하는 동시에 환경을 사용자 정의할 수 있습니다. 그러나 앱이 식사 주문 또는 식료품 쇼핑과 같이 시스템 정의 목적으로 표시되지 않는 작업을 제공하는 경우 사용자 지정 의도를 만들 수 있습니다(자세한 내용은 사용자 지정 의도 참조).
>




### **A closer look at intents**
> 의도를 더 자세히 보기
>




When people use Siri to ask questions and perform actions, Siri does the language processing and semantic analysis needed to turn their requests into intents for your app to handle. The exception is the personal phrase that people create to trigger a shortcut: When people speak the exact phrase, Siri recognizes it without doing additional processing or analysis.
> 사람들이 질문을 하고 행동을 수행하기 위해 Siri를 사용할 때, Siri는 그들의 요청을 당신의 앱이 처리할 의도로 바꾸는 데 필요한 언어 처리와 의미 분석을 한다. 바로 가기를 트리거하기 위해 사용자가 만드는 개인 구문은 예외입니다: 사람들이 정확한 문구를 말할 때, 시리는 추가적인 처리나 분석을 하지 않고 그것을 인식한다.
>




As a designer, your main job is to present clear, actionable content that helps clarify and streamline the interactions people have with Siri to get things done in your app. Some of these interactions happen while your app and SiriKit communicate about handling the intent, so it’s helpful to be familiar with the related SiriKit terminology. At a high level, your app processes an intent in three phases: resolve, confirm, and handle.
> 디자이너로서, 당신의 주요 업무는 사람들이 당신의 앱에서 일을 수행하기 위해 시리와 상호 작용하는 것을 명확히 하고 능률화하는 것을 돕는 명확하고 실행 가능한 콘텐츠를 제시하는 것이다. 이러한 상호 작용 중 일부는 당신의 앱과 SiriKit가 의도를 처리하는 것에 대해 소통하는 동안 발생하므로 관련 SiriKit 용어를 숙지하는 것이 도움이 된다. 전체적인 수준에서 앱은 해결, 확인 및 처리의 세 단계로 의도를 처리합니다.
>




First, your app and SiriKit must agree on what the request means in the *resolve* phase. You can think of this phase as the time to ask people for everything your app needs and, if necessary, ask for additional information or clarification. For example, if people ask to send a message to Amy, and they have multiple contacts named Amy, a messaging app can have Siri ask which Amy they mean. Details related to an intent, like a message recipient’s name, are known as *parameters*. In the resolve phase, you can indicate the parameters that are required to complete an action and those that are optional. For developer guidance, see [Resolving the parameters of an intent](https://developer.apple.com/documentation/sirikit/resolving_and_handling_intents/resolving_the_parameters_of_an_intent).
> 먼저, 당신의 앱과 SiriKit는 해결 단계에서 요청이 의미하는 바에 동의해야 한다. 당신은 이 단계를 당신의 앱에 필요한 모든 것을 사람들에게 요청하고, 필요한 경우 추가 정보나 설명을 요청하는 시간으로 생각할 수 있다. 예를 들어, 사람들이 Amy에게 메시지를 보내달라고 요청하고 Amy라는 이름의 여러 연락처를 가지고 있다면, 메시지 앱은 Siri가 어떤 Amy를 의미하는지 물어보도록 할 수 있습니다. 메시지 수신인의 이름과 같은 의도와 관련된 세부사항을 매개변수라고 합니다. 해결 단계에서 작업을 완료하는 데 필요한 매개 변수와 선택적인 매개 변수를 지정할 수 있습니다. 개발자 지침은 의도의 매개 변수 해결을 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/resolve-phase_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/resolve-phase_2x.png)

The second phase — called the *confirm* phase — happens when you have all the information you need to handle the intent. This phase can give people a chance to make sure they want to complete the task. For example, tasks that have financial impact require confirmation. In addition to asking for the user’s consent, you can present an error during this phase if something will prevent your app from completing the action. For example, if people use an app to order an item for pickup when the pickup location is closed, the app can describe why it can’t complete the action right now. Presenting this error during the confirm phase avoids making people wait until they’re paying for the item to find out that their request has failed. For developer guidance, see [Confirming the details of an intent](https://developer.apple.com/documentation/sirikit/resolving_and_handling_intents/confirming_the_details_of_an_intent).
> 두 번째 단계(확인 단계라고 함)는 의도를 처리하는 데 필요한 모든 정보를 가지고 있을 때 발생합니다. 이 단계는 사람들에게 그들이 그들이 그 일을 완료하기를 원하는지 확실히 할 수 있는 기회를 줄 수 있다. 예를 들어, 재정적 영향을 미치는 작업에는 확인이 필요합니다. 사용자의 동의를 구하는 것 외에도 앱이 작업을 완료하지 못하게 하는 경우 이 단계에서 오류를 표시할 수 있습니다. 예를 들어, 사람들이 픽업 위치가 닫혔을 때 앱을 사용하여 픽업할 항목을 주문하는 경우, 앱은 왜 지금 작업을 완료할 수 없는지 설명할 수 있습니다. 확인 단계에서 이 오류를 표시하면 사람들이 요청이 실패했음을 확인하기 위해 항목에 대한 비용을 지불할 때까지 기다리게 되는 것을 방지할 수 있습니다. 개발자 지침은 의도 세부사항 확인을 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/confirm-phase_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/confirm-phase_2x.png)

Third, your app performs the task and tells SiriKit what it actually did in the *handle* phase. You can provide both visual and textual information that tells people what your app did to handle their request. For example, an app that lets people order coffee might present a receipt that describes the order. Siri can speak or display the information your app provides. For developer guidance, see [Handling an intent](https://developer.apple.com/documentation/sirikit/resolving_and_handling_intents/handling_an_intent).
> 셋째, 당신의 앱은 작업을 수행하고 SiriKit에게 핸들 단계에서 실제로 무엇을 했는지 알려준다. 당신은 당신의 앱이 그들의 요청을 처리하기 위해 무엇을 했는지 사람들에게 알려주는 시각적 정보와 텍스트 정보를 모두 제공할 수 있다. 예를 들어, 사람들이 커피를 주문할 수 있는 앱은 주문을 설명하는 영수증을 제시할 수 있다. Siri는 당신의 앱이 제공하는 정보를 말하거나 표시할 수 있다. 개발자 지침은 의도 처리를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/handle-phase_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/handle-phase_2x.png)

# **Provide information about actions and support suggestions**
> 조치 및 지원 제안에 대한 정보 제공
>




Most apps enable large numbers of actions, but people tend to perform only a handful of them on a regular basis. When you tell the system about people’s regular actions and describe new ones you think they’ll want to perform in the future, Siri can *suggest* shortcuts for both types of actions when people are likely to be interested in them.
> 대부분의 앱은 많은 수의 작업을 가능하게 하지만, 사람들은 정기적으로 소수의 작업만 수행하는 경향이 있다. 당신이 사람들의 규칙적인 행동에 대해 시스템에 말하고 미래에 그들이 수행하기를 원한다고 생각하는 새로운 행동을 설명할 때, 시리는 사람들이 그것에 관심을 가질 가능성이 있을 때 두 가지 유형의 행동에 대한 바로 가기를 제안할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/suggested-action_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/suggested-action_2x.png)

For example, in an app that’s all about coffee, the most frequent action might be to order a cup of coffee, while less frequent actions might include buying coffee beans or locating a new coffee shop. In this example, the coffee app would share information about the *order coffee* action so that Siri can suggest a shortcut for this action when people usually want to do it, like weekday mornings. The app could also tell Siri about an action that people haven’t performed yet, but might be interested in — like ordering a new seasonal variation of their favorite coffee — so that Siri might suggest a shortcut for this action.
> 예를 들어, 커피와 관련된 앱에서 가장 자주 사용하는 작업은 커피 한 잔을 주문하는 것일 수 있지만, 덜 자주 사용하는 작업에는 커피 원두를 구입하거나 새 커피숍을 찾는 작업이 포함될 수 있습니다. 이 예에서 커피 앱은 주문 커피 동작에 대한 정보를 공유하여 평일 아침처럼 사람들이 보통 하고 싶을 때 시리가 이 동작에 대한 바로 가기를 제안할 수 있도록 한다. 이 앱은 또한 사람들이 아직 수행하지 않았지만 그들이 가장 좋아하는 커피의 새로운 계절적 변형을 주문하는 것과 같이 관심을 가질 수 있는 행동에 대해 시리에게 알려주어 시리가 이 행동의 지름길을 제안할 수 있다.
>




Siri can use signals like location, time of day, and type of motion (such as walking, running, or driving), to intelligently predict just the right time and place to suggest actions from your app. Depending on the information your app shares and people’s current context, Siri can offer shortcut *suggestions* on the lock screen, in search results, or on the [Siri watch face](https://support.apple.com/guide/watch/faces-and-features-apde9218b440/watchos#apdcc88df92c). Siri can also use some types of information to suggest actions that system apps support, such as using Calendar to add an event shared by your app. Here are some example scenarios.
> Siri는 위치, 하루 중 시간, 동작 유형(예: 걷기, 달리기 또는 운전)과 같은 신호를 사용하여 앱에서 동작을 제안할 수 있는 적절한 시간과 장소를 지능적으로 예측할 수 있습니다. 당신의 앱이 공유하는 정보와 사람들의 현재 상황에 따라, Siri는 잠금 화면, 검색 결과 또는 Siri 워치 페이스에서 바로 가기 제안을 제공할 수 있다. 또한 일정관리를 사용하여 앱에서 공유하는 이벤트를 추가하는 등 일부 유형의 정보를 사용하여 시스템 앱이 지원하는 작업을 제안할 수 있습니다. 다음은 몇 가지 시나리오의 예입니다.
>




- Shortly before 7:30 a.m., Siri might suggest the *order coffee* action to people who use the coffee app every morning.
- >  오전 7시 30분 조금 전, 시리는 매일 아침 커피 앱을 사용하는 사람들에게 커피 주문 행동을 제안할지도 모른다.

- After people use a box office–type app to buy tickets to a movie, Siri might remind them to turn on Do Not Disturb shortly before showtime.
- >  사람들이 영화 티켓을 사기 위해 박스 오피스 형태의 앱을 사용한 후, 시리는 그들에게 상영 시간 직전에 방해하지 말라고 상기시킬 수 있다.

