# **[patterns] workouts**

# A great workout or fitness experience encourages people to focus on their current activity and helps them track their progress on their devices.
> 훌륭한 운동이나 피트니스 경험은 사람들이 현재 활동에 집중하도록 격려하고 그들이 그들의 장치에서 그들의 진행 상황을 추적하도록 돕는다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-workouts-intro-dark_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/patterns/pattern-workouts-intro-dark_2x.png)

People can wear their Apple Watch during many types of workouts, and they might carry their iPhone or iPad during fitness activities like walking, wheelchair pushing, and running. In contrast, people tend to use their larger or more stationary devices like iPad Pro, Mac, and Apple TV to participate in live or recorded workout sessions by themselves or with others.
> 사람들은 많은 종류의 운동을 하는 동안 애플워치를 착용할 수 있고, 걷기, 휠체어 밀기, 달리기 같은 피트니스 활동 동안 아이폰이나 아이패드를 휴대할 수도 있다. 대조적으로, 사람들은 아이패드 프로, 맥, 애플 TV와 같은 더 크거나 더 많은 고정 장치를 사용하여 라이브 또는 녹음된 운동 세션에 참여하거나 다른 사람들과 함께 참여하는 경향이 있다.
>




You can create a workout experience for Apple Watch, iPhone, or iPad that helps people reach their goals by leveraging activity data from the device and using familiar components to display fitness metrics.
> 장치의 활동 데이터를 활용하고 익숙한 구성 요소를 사용하여 피트니스 메트릭을 표시하여 사람들이 목표를 달성할 수 있도록 도와주는 Apple Watch, iPhone 또는 iPad의 운동 환경을 만들 수 있습니다.
>




# **Best practices**

**In a watchOS fitness app, use workout sessions to provide useful data and relevant controls.** During a fitness app’s active workout sessions, watchOS continues to display the app as time passes between wrist raises, so it’s important to provide the workout data people are most likely to care about. For example, you might show elapsed or remaining time, calories burned, or distance traveled, and offer relevant controls like lap or interval markers.
> 시계로OS 피트니스 앱, 유용한 데이터와 관련 컨트롤을 제공하기 위해 운동 세션을 사용합니다. 피트니스 앱의 활동적인 운동 시간 동안, 보세요.OS는 손목 상승 사이의 시간이 지날수록 앱을 계속 표시하기 때문에 사람들이 가장 신경 쓸 만한 운동 데이터를 제공하는 것이 중요하다. 예를 들어 경과된 시간 또는 남은 시간, 연소된 칼로리 또는 이동 거리를 표시하고 랩 또는 간격 표시기와 같은 관련 컨트롤을 제공할 수 있습니다.
>




**Avoid distracting people from a workout with information that’s not relevant.** For example, people don’t need to review the list of workouts you offer or access other parts of your app while they’re working out. Here is an arrangement that many watchOS workout apps use, including Workout:
> 관련이 없는 정보로 운동하는 사람들을 산만하게 하는 것을 피하세요. 예를 들어, 사람들은 운동하는 동안 당신이 제공하는 운동 목록을 검토하거나 앱의 다른 부분에 액세스할 필요가 없습니다. 여기 많은 사람들이 지켜보는 배열이 있다.워크아웃을 포함한 OS 워크아웃 앱 사용:
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/workouts/images/workouts-large-buttons_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/workouts/images/workouts-large-buttons_2x.png)

Large buttons that control the in-progress session — such as Pause, Resume, and End — appear on the leftmost screen.
> 진행 중인 세션을 제어하는 큰 단추(예: 일시 중지, 재개 및 종료)가 맨 왼쪽 화면에 나타납니다.
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/workouts/images/workouts-metrics_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/workouts/images/workouts-metrics_2x.png)

Metrics and other data appear on a dedicated screen that people can read at a glance.
> 메트릭스 및 기타 데이터는 사람들이 한 눈에 읽을 수 있는 전용 화면에 나타납니다.
>




![https://developer.apple.com/design/human-interface-guidelines/patterns/workouts/images/workouts-media-playback_2x.png](https://developer.apple.com/design/human-interface-guidelines/patterns/workouts/images/workouts-media-playback_2x.png)

If supported, media playback controls appear on the rightmost screen.
> 지원되는 경우 미디어 재생 컨트롤이 맨 오른쪽 화면에 나타납니다.
>




**Use a distinct visual appearance to indicate an active workout.** During a workout, people appreciate being able to recognize an active session at a glance. The metrics page can be a good way to show that a session is active because the values update in real time. In addition to displaying updating values, you can further distinguish the metrics screen by using a unique layout.
> 활동적인 운동을 나타내기 위해 뚜렷한 시각적 외관을 사용하세요. 운동하는 동안, 사람들은 한 눈에 활동적인 세션을 인식할 수 있다는 것에 감사한다. 메트릭 페이지는 값이 실시간으로 업데이트되기 때문에 세션이 활성 상태임을 보여주는 좋은 방법이 될 수 있습니다. 업데이트 값을 표시하는 것 외에도 고유한 레이아웃을 사용하여 메트릭 화면을 추가로 구분할 수 있습니다.
>




**Provide workout controls that are easy to find and tap.** In addition to making it easy for people to pause, resume, and stop a workout, be sure to provide clear feedback that indicates when a session starts or stops.
> 쉽게 찾고 두드리기 쉬운 운동 컨트롤을 제공하세요. 사람들이 운동을 일시 중지, 재개 및 중지하는 것을 쉽게 할 뿐만 아니라, 세션이 언제 시작되거나 중지되는지 나타내는 명확한 피드백을 제공해야 한다.
>




**Help people understand the health information your app records if sensor data is unavailable during a workout.** For example, water may prevent a heart-rate measurement, but your app can still record data like the distance people swam and the number of calories they burned. If your app supports the *Swimming* or *Other* workout types, explain the situation using language that’s similar to the language used in the system-provided Workout app, as shown below:
> 운동 중에 센서 데이터를 사용할 수 없는 경우 앱에서 기록하는 건강 정보를 사람들이 이해할 수 있도록 도와줍니다. 예를 들어, 물은 심박수 측정을 방해할 수 있지만, 당신의 앱은 여전히 사람들이 수영한 거리나 그들이 태운 칼로리와 같은 데이터를 기록할 수 있다. 프로그램이 수영 또는 기타 운동 유형을 지원하는 경우 시스템에서 제공하는 운동 앱에 사용되는 언어와 유사한 언어를 사용하여 다음과 같이 상황을 설명합니다.
>




[제목 없음](https://www.notion.so/0abb59676f00496786827a8cc580ed7c)

**Provide a summary at the end of a session.** A summary screen confirms that a workout is finished and displays the recorded information. Consider enhancing the summary by including Activity rings, so that people can easily check their current progress.
> 세션이 끝날 때 요약을 제공합니다. 요약 화면에 운동이 완료되었음을 확인하고 기록된 정보가 표시됩니다. 사람들이 현재 진행 상황을 쉽게 확인할 수 있도록 활동 링을 포함하여 요약을 개선하는 것을 고려해 보십시오.
>




**Discard extremely brief workout sessions.** If a session ends a few seconds after it starts, either discard the data automatically or ask people if they want to record the data as a workout.
> 극도로 짧은 운동 시간을 버리세요. 세션이 시작된 지 몇 초 후에 종료되는 경우, 데이터를 자동으로 삭제하거나 사람들에게 데이터를 운동으로 기록할지 여부를 묻습니다.
>




**Make sure text is legible for when people are in motion.** When a session requires movement, use large font sizes, high-contrast colors, and arrange text so that the most important information is easy to read.
> 사람이 움직일 때 텍스트를 읽을 수 있는지 확인하십시오. 세션에 이동이 필요한 경우 큰 글꼴 크기와 고대비 색상을 사용하고 가장 중요한 정보를 읽기 쉽도록 텍스트를 정렬합니다.
>




**Use Activity rings correctly.** The Activity rings view is an Apple-designed element featuring one or more rings whose colors and meanings match those in the Activity app. Use them only for their documented purpose.
> 활동 링을 올바르게 사용합니다. 활동 링 보기는 활동 앱의 링과 색상 및 의미가 일치하는 하나 이상의 링을 특징으로 하는 Apple 설계 요소입니다. 문서화된 용도로만 사용하십시오.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, or watchOS. Not supported in macOS or tvOS.*
> iOS, iPadOS 또는 watch OS에 대한 추가 고려 사항은 없습니다. macOS 또는 tvOS에서는 지원되지 않습니다.
>



