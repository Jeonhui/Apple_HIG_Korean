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

- Siri might suggest an automation that starts a workout in the user’s favorite workout app and plays their favorite workout playlist as they enter their usual gym.
- >  시리는 사용자가 가장 좋아하는 운동 앱에서 운동을 시작하고 그들이 평소 사용하던 체육관에 들어갈 때 가장 좋아하는 운동 재생 목록을 재생하는 자동화를 제안할 수 있다.

- When people enter the airport after a home-bound flight, Siri might suggest they request a ride home from their favorite ride-sharing app.
- >  사람들이 집으로 향하는 비행기를 타고 공항에 들어갈 때, 시리는 그들이 가장 좋아하는 승차 공유 앱에서 집으로 태워달라고 제안할 수 있다.


When you provide information about your actions to the system, people can also use the Shortcuts app to create shortcuts for the system and custom intents you support. For guidance, see [Shortcuts and suggestions](../technologies/siri/shortcuts-and-suggestions/).
> 작업에 대한 정보를 시스템에 제공하면 바로 가기 앱을 사용하여 지원하는 시스템 및 사용자 지정 의도에 대한 바로 가기를 만들 수도 있습니다. 자세한 내용은 바로 가기 및 제안을 참조하십시오.
>




# **Design a great voice experience**
> 뛰어난 음성 환경 설계
>




A great voice interface helps people feel confident they’ll get the results they want, even when they’re not sure what they can say. Siri supports different voice experiences for system-provided intents and custom intents. With a system intent, Siri does the natural language processing for you, letting people interact with your app in various conversational ways. With a custom intent, your app helps people perform a task that Siri doesn’t know about yet, which results in a different type of support for the voice experience. Custom intents give you additional opportunities to customize conversational dialogue, but also require people to create and speak a precise phrase to trigger the interaction.
> 훌륭한 음성 인터페이스는 사람들이 그들이 무엇을 말할 수 있는지 확신할 수 없을 때에도 그들이 원하는 결과를 얻을 것이라고 확신하도록 도와준다. Siri는 시스템 제공 의도와 사용자 정의 의도를 위해 다양한 음성 경험을 지원합니다. 시스템 의도로, Siri는 사람들이 다양한 대화 방식으로 당신의 앱과 상호 작용할 수 있도록 당신을 위해 자연어 처리를 한다. 사용자 지정 의도를 가진 당신의 앱은 사람들이 시리가 아직 알지 못하는 작업을 수행하도록 도와주므로 음성 경험에 대한 다른 유형의 지원을 제공한다. 사용자 정의 의도는 대화 대화를 사용자 정의할 수 있는 추가적인 기회를 제공하지만 사용자가 상호 작용을 트리거하기 위해 정확한 구문을 만들고 말해야 합니다.
>




As a designer, you have several ways to enhance both types of conversational experiences and help people specify what they want without engaging in lengthy exchanges.
> 디자이너로서, 당신은 두 가지 유형의 대화 경험을 향상시키고 사람들이 긴 교환에 참여하지 않고 그들이 원하는 것을 지정하도록 돕는 몇 가지 방법을 가지고 있다.
>




For system-provided intents, you help Siri communicate with people about the action they want to accomplish by providing essential information and defining any app-specific terminology that might come up during the conversation. You don’t have to write additional dialogue for Siri to speak because Siri already knows about the actions in the system-defined domains and understands many ways that people may talk about them. For example, if you need to confirm the recipient’s name during the resolve phase of a messaging intent, you simply indicate that the required parameter value is missing and Siri says to the sender "Who do you want to send it to?"
> 시스템 제공 목적을 위해 Siri는 필수 정보를 제공하고 대화 중에 나타날 수 있는 앱별 용어를 정의하여 사람들이 원하는 작업에 대해 소통할 수 있도록 도와줍니다. Siri는 이미 시스템 정의 도메인의 동작에 대해 알고 있고 사람들이 그것에 대해 말할 수 있는 많은 방법을 이해하고 있기 때문에 Siri가 말하기 위해 추가 대화를 작성할 필요가 없다. 예를 들어, 메시징 의도 해결 단계에서 수신자의 이름을 확인해야 하는 경우, 필요한 매개 변수 값이 누락되었음을 표시하고 Siri는 발신자에게 "누구에게 보낼 것입니까?"라고 말합니다
>




Even though you don’t write custom dialogue for system-provided intents, you can enhance the voice experience in other ways. For example, if people ask Siri to "play *Your Music App*" as they enter their gym, you could respond by playing their workout playlist.
> 시스템에서 제공하는 용도로 사용자 지정 대화를 작성하지 않더라도 다른 방법으로 음성 경험을 향상시킬 수 있습니다. 예를 들어, 만약 사람들이 체육관에 들어갈 때 시리에게 "당신의 음악 앱을 틀어달라"고 요청한다면, 당신은 그들의 운동 재생 목록을 재생함으로써 응답할 수 있다.
>




When you support a custom intent, people initiate the action by using their personal invocation phrase; if people don’t speak their phrase precisely, Siri doesn’t trigger the intent. Although you can suggest a memorable phrase for people to use, your principal job is to write clear, direct dialogue, often in the form of follow-up questions, to help people accomplish the action in as few steps as possible.
> 사용자 정의 의도를 지지할 때, 사람들은 개인적인 호출 문구를 사용하여 행동을 시작합니다. 사람들이 그들의 문구를 정확하게 말하지 않으면, 시리는 의도를 유발하지 않습니다. 비록 여러분이 사람들이 사용해야 할 기억할 만한 문구를 제안할 수 있지만, 여러분의 주된 일은 사람들이 가능한 몇 단계로 행동을 완수하도록 돕기 위해 종종 후속 질문의 형태로 명확하고 직접적인 대화를 쓰는 것입니다.
>




For example, a coffee app might suggest *Order coffee* as a phrase people could use to reorder a favorite cup of coffee. In a scenario where people usually use *Order coffee* to order a cappuccino in various sizes, the coffee app could follow up with custom dialogue that builds on this knowledge, like "What size of cappuccino?" For other types of actions, more open-ended questions can be better at helping people accomplish the task efficiently. For example, if people trigger a grocery shopping action by saying *Add to cart*, the grocery shopping app could follow up with "OK, what do you want?"
> 예를 들어, 커피 앱은 사람들이 좋아하는 커피를 주문할 때 사용할 수 있는 문구로 커피 주문을 제안할 수 있다. 보통 주문커피를 이용해 다양한 크기의 카푸치노를 주문하는 시나리오에서 커피 앱은 '카푸치노 사이즈는?'와 같은 이 지식을 바탕으로 한 맞춤형 대화로 후속할 수 있다 다른 유형의 행동의 경우, 더 자유로운 질문은 사람들이 작업을 효율적으로 수행하도록 돕는 데 더 효과적일 수 있다. 예를 들어, 만약 사람들이 카트에 추가라고 말하면서 식료품 쇼핑 행동을 촉발시킨다면, 식료품 쇼핑 앱은 "좋아, 너는 무엇을 원하니?"로 후속 조치를 할 수 있다
>




# **Recognize that people use Siri in different contexts**
> 사람들이 다양한 맥락에서 시리를 사용한다는 것을 인식합니다
>




People can use Siri to get things done while they’re in a car, working out, using apps on a device, or interacting with HomePod. You don’t always know the context in which people are using Siri to perform your app’s actions, so flexibility is key in order to help people have a great experience no matter what they’re doing.
> 사람들은 차 안에 있거나, 운동을 하거나, 기기의 앱을 사용하거나, 홈팟과 상호 작용하는 동안 시리를 사용하여 일을 끝낼 수 있다. 사용자가 Siri를 사용하여 앱의 작업을 수행하는 상황을 항상 알 수 있는 것은 아니므로, 사용자가 무엇을 하든 훌륭한 경험을 할 수 있도록 하려면 유연성이 중요합니다.
>




To communicate with people regardless of their current context, you should supply information that Siri can provide both vocally and visually. Supporting both voice and screen-based content lets Siri decide which communication method works best for people in their current situation. For example, Siri speaks to people through their AirPods if they say "Hey Siri" while using them.
> 현재 상황에 상관없이 사람들과 소통하기 위해서는 시리가 음성적으로나 시각적으로 제공할 수 있는 정보를 제공해야 한다. 음성과 화면 기반 콘텐츠를 모두 지원함으로써 시리는 현재 상황에 있는 사람들에게 가장 적합한 의사소통 방법을 결정할 수 있다. 예를 들어, 사람들이 에어팟을 사용하면서 "안녕 시리"라고 말하면 시리는 에어팟을 통해 사람들에게 말한다.
>




In voice-only situations, Siri verbally describes information that would have been presented onscreen in other situations. Consider a food-delivery app that requires people to confirm a transaction before completing the order. In a voice-only scenario, Siri may say "Your total is fifteen dollars, and your order will take thirty minutes to arrive at your door. Ready to order?" In contrast, when people can view the cost and delivery information onscreen, Siri might simply say "Ready to order?" When you support custom intents, you’re responsible for supplying the voice-only dialogue that describes these types of onscreen information.’
> 음성 전용 상황에서 시리는 다른 상황에서 화면에 표시되었을 정보를 구두로 설명합니다. 주문을 완료하기 전에 사람들이 거래를 확인하도록 요구하는 음식 배달 앱을 생각해보세요. 음성 전용 시나리오에서 시리는 "총 15달러이며, 주문하신 물건이 문 앞에 도착하는 데 30분이 걸릴 것입니다. 주문하시겠습니까?" 대조적으로, 사람들이 가격과 배송 정보를 화면에서 볼 수 있을 때, 시리는 단순히 "주문 준비가 되었습니까?"라고 말할 수 있다 사용자 지정 의도를 지원할 때는 이러한 유형의 화면 정보를 설명하는 음성 전용 대화를 제공해야 합니다.'
>



