# **[technologies] shazamkit**

# ShazamKit enables audio recognition by matching an audio sample against the ShazamKit catalog or a custom audio catalog.
> ShazamKit은 오디오 샘플을 ShazamKit 카탈로그 또는 사용자 정의 오디오 카탈로그와 대조하여 오디오 인식을 가능하게 한다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-ShazamKit-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/technologies/technology-ShazamKit-intro_2x.png)

You can use ShazamKit to enable features like:
> ShazamKit을 사용하여 다음과 같은 기능을 사용할 수 있습니다:
>




- Enhancing experiences with graphics that correspond with the genre of currently playing music
- >  현재 재생 중인 음악의 장르에 해당하는 그래픽으로 경험 향상

- Making media content accessible to people with hearing disabilities by providing closed captions or sign language that syncs with the audio
- >  오디오와 동기화되는 폐쇄 캡션 또는 수화를 제공하여 청각 장애인이 미디어 콘텐츠에 액세스할 수 있도록 함

- Synchronizing in-app experiences with virtual content in contexts like online learning and retail
- >  온라인 학습 및 소매와 같은 맥락에서 앱 내 경험을 가상 콘텐츠와 동기화


If you need the device microphone to get audio samples for your app to recognize, you must request access to it. As with all types of permission requests, it’s important to help people understand why you’re asking for access. For guidance, see [Accessing private data](../patterns/accessing-private-data).
> 앱이 인식할 수 있는 오디오 샘플을 가져오는 데 장치 마이크가 필요한 경우 해당 마이크에 대한 액세스를 요청해야 합니다. 모든 유형의 사용 권한 요청과 마찬가지로 사용자가 액세스를 요청하는 이유를 사람들이 이해할 수 있도록 돕는 것이 중요합니다. 자세한 내용은 개인 데이터 액세스를 참조하십시오.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/shazamkit/images/mic-permission_2x.png](https://developer.apple.com/design/human-interface-guidelines/technologies/shazamkit/images/mic-permission_2x.png)

# **Best practices**

After you receive permission to access the microphone for features that have ShazamKit enabled, follow these guidelines.
> ShazamKit이 활성화된 기능에 대한 마이크 액세스 권한을 받은 후 다음 지침을 따르십시오.
>




**Stop recording as soon as possible.** When people allow your app to record audio for recognition, they don’t expect the microphone to stay on. To help preserve privacy, only record for as long as it takes to get the sample you need.
> 사람들이 인식을 위해 앱에서 오디오를 녹음하도록 허용하면 마이크가 계속 켜져 있을 것으로 예상하지 못합니다. 개인 정보 보호를 위해 필요한 샘플을 얻는 데 걸리는 시간 동안만 기록하십시오.
>




**Let people opt in to storing your app’s recognized songs to their iCloud library.** If your app can store recognized songs to iCloud, give people a way to first approve this action. Even though both the Music Recognition control and the Shazam app show your app as the source of the recognized song, people appreciate having control over which apps can store content in their library.
> 사용자가 앱의 인식된 노래를 iCloud 라이브러리에 저장하도록 선택할 수 있습니다. 인식된 노래를 앱이 iCloud에 저장할 수 있다면 먼저 사용자에게 이 작업을 승인할 수 있는 방법을 제공하십시오. 음악 인식 컨트롤과 Shazam 앱 모두 당신의 앱을 인식된 노래의 소스로 보여주지만, 사람들은 어떤 앱이 그들의 라이브러리에 콘텐츠를 저장할 수 있는지를 제어하는 것에 감사한다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*
> iOS, iPadOS, macOS, tvOS 또는 시계에 대한 추가 고려 사항 없음운영 체제.
>



