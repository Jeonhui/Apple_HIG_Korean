# **[technologies-siri] system-intents**

SiriKit defines a large number of system intents that represent common tasks people do, such as playing music, sending messages to friends, and managing notes. For system intents, Siri defines the conversational flow, while your app provides the data to complete the interaction.
> SiriKit은 음악 재생, 친구에게 메시지 보내기, 노트 관리와 같은 사람들이 하는 일반적인 작업을 나타내는 많은 수의 시스템 의도를 정의한다. 시스템 목적을 위해 Siri는 대화 흐름을 정의하고, 당신의 앱은 상호 작용을 완료하기 위한 데이터를 제공한다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/sirikit-intent-hero_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/sirikit-intent-hero_2x.png)

SiriKit provides the following intents.

| Domain(link to developer guidance) | Intents |
| --- | --- |
| https://developer.apple.com/documentation/sirikit/voip_calling | Initiate calls. |
| https://developer.apple.com/documentation/sirikit/workouts | Start, pause, resume, end, and cancel workouts. |
| https://developer.apple.com/documentation/sirikit/lists_and_notes | Create notes.Search for notes.Create reminders based on a date, time, or location. |
| https://developer.apple.com/documentation/sirikit/media | Search for and play media content, such as video, music, audiobooks, and podcasts.Like or dislike items.Add items to a library or playlist. |
| https://developer.apple.com/documentation/sirikit/messaging | Send messages.Search for messages.Read received messages. |
| https://developer.apple.com/documentation/sirikit/payments | Send payments.Request payments. |
| https://developer.apple.com/documentation/sirikit/car_commands | Activate hazard lights or honk the horn.Lock and unlock the doors.Check the current fuel or power level. |

# **Design responses to system intents**
> 시스템 의도에 대한 응답 설계
>




People use Siri for convenience and they expect a fast response. Your app should perform the system intents it supports quickly and accurately so that people have a great experience when they choose your app to get things done.
> 사람들은 편의상 시리를 사용하고 빠른 대응을 기대한다. 당신의 앱은 지원하는 시스템 의도를 빠르고 정확하게 수행하여 사람들이 당신의 앱을 선택할 때 훌륭한 경험을 할 수 있도록 해야 한다.
>




**Complete requests without leaving Siri whenever possible.** If a request must be finished in your app, take people directly to the expected destination. Don’t show intermediary screens or messages that slow down the experience.
> 가능한 한 시리를 떠나지 않고 요청을 완료하십시오. 앱에서 요청을 완료해야 하는 경우, 사람들을 예상 목적지로 직접 데려가십시오. 경험을 느리게 하는 중간 화면이나 메시지를 표시하지 마십시오.
>




**When a request has a financial impact, default to the safest and least expensive option.**Never deceive people or misrepresent information. For a purchase with multiple pricing levels, don’t default to the most expensive. When people make a payment, don’t charge extra fees without informing them.
> 요청이 재정적 영향을 미치는 경우 가장 안전하고 비용이 적게 드는 옵션으로 기본 설정합니다.절대로 사람들을 속이거나 정보를 잘못 전달하지 마세요. 가격 수준이 여러 개인 구매의 경우 가장 비싼 것으로 기본 설정하지 마십시오. 사람들이 결제할 때, 그들에게 알리지 않고 추가 요금을 청구하지 마세요.
>




**When people request media playback from your app, consider providing alternative results if the request is ambiguous.** When you display alternative results within the Siri UI, people can easily choose a different piece of content if your first offering isn’t what they want.
> 사용자가 앱에서 미디어 재생을 요청할 때 요청이 모호할 경우 대체 결과를 제공하는 것을 고려하십시오. Siri UI 내에서 대체 결과를 표시할 때 첫 번째 제안이 원하는 것이 아니라면 다른 콘텐츠를 쉽게 선택할 수 있습니다.
>




**On Apple Watch, design a streamlined workflow that requires minimal interaction.** Use intelligent defaults instead of asking for input whenever possible. For example, a music app could respond to a nonspecific request — such as "Play music with MyMusicApp" — by playing a favorite playlist. If you must present options to people, offer a small number of focused choices that reduce the need for additional prompting.
> Apple Watch에서는 상호 작용을 최소화하는 간소화된 워크플로우를 설계합니다. 가능한 한 입력을 요청하는 대신 지능형 기본값을 사용하십시오. 예를 들어 음악 앱은 "MyMusicApp으로 음악 재생"과 같은 특정하지 않은 요청에 즐겨찾기 재생 목록을 재생하여 응답할 수 있습니다. 사용자에게 선택사항을 제시해야 하는 경우, 추가 프롬프트의 필요성을 줄이는 소수의 집중적인 선택사항을 제공하십시오.
>




# **Enhance the voice experience for system intents**
> 시스템 용도에 맞는 음성 환경 개선
>




Help people learn how to use Siri to get things done in your app and make conversation with Siri feel natural in the context of your brand by defining app-specific terms and alternative ways people might refer to your app.
> 앱별 용어와 사용자가 앱을 참조할 수 있는 대체 방법을 정의하여 사람들이 Siri를 사용하여 앱에서 작업을 수행하는 방법을 배우고 브랜드 맥락에서 Siri와의 대화를 자연스럽게 느끼도록 도와줍니다.
>




**Create example requests.** When people tap the Help button in the Siri interface, they view a guide that can include example phrases that you supply. Write phrases that demonstrate the easiest and most efficient ways to use Siri with your app. For developer guidance, see [Intent phrases](https://developer.apple.com/documentation/sirikit/registering_custom_vocabulary_with_sirikit/global_vocabulary_reference/intent_phrases).
> 예제 요청 만들기. 사용자가 Siri 인터페이스에서 도움말 버튼을 누르면 사용자가 제공하는 예제 구문을 포함할 수 있는 가이드가 표시됩니다. 당신의 앱으로 시리를 가장 쉽고 효율적으로 사용하는 방법을 보여주는 문구를 작성하세요. 개발자 지침은 의도 구문을 참조하십시오.
>




**Define custom vocabulary that people use with your app.** Help Siri learn more about the actions your app performs by defining specific terms people might actually use in requests, like account names, contact names, photo tags, photo album names, ride options, and workout names. Make sure these terms are nongeneric and unique to your app. Never include other app names, terms that are obviously connected with other apps, inappropriate language, or reserved phrases, such as *Hey Siri*. Note that Siri uses the terms you define to help resolve requests, but there’s no guarantee that Siri will recognize them.
> Siri는 계정 이름, 연락처 이름, 사진 태그, 사진 앨범 이름, 승차 옵션 및 운동 이름과 같은 요청에서 사용자가 실제로 사용할 수 있는 특정 용어를 정의하여 앱이 수행하는 작업에 대해 자세히 알아볼 수 있습니다. 이러한 용어가 일반적이지 않고 앱에 고유한지 확인하십시오. 다른 앱 이름, 다른 앱과 연결된 용어, 부적절한 언어 또는 예약된 문구(예: Hey Siri)를 포함하지 마십시오. 사용자가 정의한 용어를 사용하여 요청을 해결하지만 Siri가 이를 인식한다는 보장은 없습니다.
>




**Consider defining alternative app names.** If people might refer to your app in different ways, it’s a good idea to provide a list of alternative names to help Siri understand what people mean. For example, a UnicornChat app might define the term *Unicorn* as an alternative app name. Never impersonate other apps by listing their names as alternative names for your app.
> 다른 앱 이름을 정의하는 것을 고려해 보십시오. 사람들이 다른 방식으로 앱을 참조할 수 있다면 Siri가 사람들의 의미를 이해하는 데 도움이 되도록 대체 이름 목록을 제공하는 것이 좋습니다. 예를 들어, UnicornChat 앱은 Unicorn이라는 용어를 대체 앱 이름으로 정의할 수 있습니다. 다른 앱의 이름을 앱의 대체 이름으로 나열하여 다른 앱을 가장하지 마십시오.
>




# **Design a custom interface for a system intent**
> 시스템 용도에 맞는 사용자 지정 인터페이스 설계
>




If it makes sense in your iOS app, you can supply custom interface elements or a completely custom UI for Siri or Maps to display along with your intent response. A watchOS app can’t provide a custom UI for Siri to display on Apple Watch.
> iOS 앱에서 사용자 지정 인터페이스 요소 또는 Siri 또는 Maps가 의도 응답과 함께 표시할 완전한 사용자 지정 UI를 제공할 수 있습니다. 시계OS 앱은 시리가 애플 워치에 표시할 수 있는 사용자 지정 UI를 제공할 수 없습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-in-siri-interface_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-in-siri-interface_2x.png)

**Avoid including extraneous or redundant information.** A custom interface lets you bring elements from your app into the Siri interface, but displaying information that isn’t related to the action can distract people. You also want to avoid duplicating information that the system can display in the Siri or Maps interface. For developer guidance, see [INParameter](https://developer.apple.com/documentation/sirikit/inparameter).
> 사용자 지정 인터페이스를 사용하면 앱의 요소를 Siri 인터페이스로 가져올 수 있지만, 작업과 관련이 없는 정보를 표시하면 사람들의 주의를 분산시킬 수 있습니다. 또한 시스템이 Siri 또는 Maps 인터페이스에 표시할 수 있는 정보가 중복되지 않도록 해야 합니다. 개발자 지침은 IN 매개 변수를 참조하십시오.
>




**Make sure people can still perform the action without viewing your custom interface.** People can switch to voice-only interaction with Siri at any time, so it’s crucial to help Siri speak the same information that you display in your custom interface.
> 사용자 지정 인터페이스를 보지 않고도 작업을 수행할 수 있는지 확인하십시오. 사용자는 언제든지 Siri와 음성 전용 상호 작용으로 전환할 수 있으므로 Siri가 사용자 지정 인터페이스에 표시되는 것과 동일한 정보를 말할 수 있도록 돕는 것이 중요합니다.
>




**Use ample margins and padding in your custom interface.** Avoid extending content to the edges of your interface unless it’s content that appears to flow naturally offscreen, like a map. In general, provide a margin of 20 points between each edge of your interface and the content. Use the app icon that appears above your interface to guide alignment: content tends to look best when it’s lined up with the center of this icon.
> 사용자 지정 인터페이스에서 충분한 여백과 패딩을 사용하십시오. 지도처럼 화면 밖으로 자연스럽게 흘러가는 콘텐츠가 아닌 경우에는 콘텐츠를 인터페이스 가장자리로 확장하지 마십시오. 일반적으로 인터페이스의 각 가장자리와 내용 사이에 20점의 여백을 제공합니다. 인터페이스 위에 나타나는 앱 아이콘을 사용하여 정렬을 안내합니다. 콘텐츠는 이 아이콘의 중앙에 정렬할 때 가장 잘 보이는 경향이 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-insets_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-insets_2x.png)

**Minimize the height of your interface.** The system displays other elements above and below your custom interface, such as the text prompt, the spoken response, and the Siri waveform. Aim for a custom interface height that’s no taller than half the height of the screen, so people can see all your content without scrolling.
> 인터페이스 높이를 최소화합니다. 시스템은 텍스트 프롬프트, 음성 응답 및 Siri 파형과 같은 다른 요소를 사용자 지정 인터페이스 위와 아래에 표시합니다. 화면 높이의 절반 이하인 사용자 지정 인터페이스 높이를 목표로 하여 스크롤하지 않고도 모든 콘텐츠를 볼 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-height_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/images/custom-ui-height_2x.png)

**Refrain from displaying your app name or icon.** The system automatically shows this information, so it’s redundant to include it in your custom interface.
> 앱 이름이나 아이콘을 표시하지 마십시오. 시스템에서 자동으로 이 정보를 표시하므로 사용자 지정 인터페이스에 포함하는 것이 중복됩니다.
>




For developer guidance, see [Creating an intents UI extension](https://developer.apple.com/documentation/sirikit/creating_an_intents_ui_extension).
> 개발자 지침은 의도 UI 확장 만들기를 참조하십시오.
>



