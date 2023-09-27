# **[technologies-homekit] setup**

The Home app makes it easy for people to discover, add, name, and specify the location of accessories. Even if your accessory requires additional custom setup, you can take advantage of the system-provided setup flow.
> 홈 앱을 사용하면 사람들이 액세서리의 위치를 쉽게 검색, 추가, 이름 지정 및 지정할 수 있습니다. 액세서리에 추가 사용자 지정 설정이 필요한 경우에도 시스템에서 제공하는 설정 흐름을 활용할 수 있습니다.
>




# **Streamline the setup experience**

**Use the system-provided setup flow to give users a familiar experience.** The HomeKit setup flow works more quickly than traditional setup flows because it lets people name accessories, join networks, pair with HomeKit, assign room and service categories, and designate favorites in just a few steps. Using the system-provided setup flow also lets your app focus on promoting the custom functionality that makes your accessory unique. For developer guidance, see the [HMHome method](https://developer.apple.com/documentation/homekit/hmhome/2941039-addandsetupaccessories)for adding accessories.
> 시스템에서 제공하는 설정 흐름을 사용하여 사용자에게 친숙한 경험을 제공합니다. HomeKit 설정 흐름은 사람들이 액세서리의 이름을 지정하고, 네트워크에 가입하고, HomeKit와 쌍을 이루고, 룸과 서비스 범주를 할당하고, 몇 단계만 거치면 즐겨찾기를 지정할 수 있기 때문에 기존 설정 흐름보다 더 빠르게 작동합니다. 또한 시스템에서 제공하는 설정 흐름을 사용하면 앱이 액세서리를 고유하게 만드는 사용자 지정 기능을 홍보하는 데 집중할 수 있습니다. 개발자 지침은 HMHome 방법에서 액세서리를 추가하는 방법을 참조하십시오.
>




**Provide context to explain why you need access to people's Home data.** Create a purpose string with a phrase that describes why you’re asking for the user’s permission to access their data, such as "Enables you to control this accessory with the Apple Home app and Siri across your Apple devices."
> 사용자의 홈 데이터에 액세스해야 하는 이유를 설명하는 컨텍스트를 제공하십시오. "Apple Home 앱으로 이 액세서리를 제어하고 Apple 장치 전체에서 Siri를 제어할 수 있습니다."와 같이 사용자의 데이터에 액세스할 수 있는 사용자 권한을 요청하는 이유를 설명하는 문구가 포함된 목적 문자열을 만듭니다
>




**Don't require people to create an account or supply personal information.** Instead, defer to HomeKit for any information you might need. If your app provides additional services that require an account, such as cloud services, make account setup optional and wait until after initial HomeKit setup to offer it.
> 계정을 만들거나 개인 정보를 제공하도록 사용자에게 요구하지 마십시오. 대신 필요한 정보는 HomeKit을 사용하십시오. 앱에서 클라우드 서비스와 같이 계정이 필요한 추가 서비스를 제공하는 경우 계정 설정을 선택 사항으로 지정하고 초기 홈킷 설정이 완료될 때까지 기다립니다.
>




**Honor the user’s setup choice.** When people choose to use HomeKit to set up your accessory, don’t force them to set up other platforms during the HomeKit setup flow. A cross-platform setup experience prevents people from using the accessory right away and can cause confusion by presenting too many ways to control the accessory.
> 사용자의 설정 선택을 존중하십시오. 사용자가 홈킷을 사용하여 액세서리를 설정할 때 홈킷 설정 흐름 중에 다른 플랫폼을 설정하도록 강요하지 마십시오. 크로스 플랫폼 설정 경험은 사람들이 액세서리를 바로 사용하는 것을 막고 액세서리를 제어하는 방법을 너무 많이 제시해 혼란을 일으킬 수 있다.
>




**Carefully consider how and when to provide a custom accessory setup experience.** Always begin by presenting the system-provided setup flow. Then, after the accessory's basic functionality is enabled, offer a custom post-setup experience that highlights the unique features of your accessory and helps people get the most out of it. For example, a light manufacturer's app could help people create personalized light scenes in their homes using key colors scanned in from photos in their library.
> 사용자 지정 액세서리 설정 경험을 제공하는 방법과 시기를 신중하게 고려하십시오. 항상 시스템에서 제공하는 설정 흐름을 제시하는 것부터 시작하십시오. 그런 다음 액세서리의 기본 기능을 활성화한 후 액세서리의 고유한 기능을 강조하고 사용자가 액세서리를 최대한 활용할 수 있도록 지원하는 사용자 지정 설정 후 환경을 제공합니다. 예를 들어, 한 조명 제조업체의 앱은 사람들이 도서관의 사진에서 스캔한 주요 색상을 사용하여 가정에서 개인화된 조명 장면을 만들 수 있도록 도와줄 수 있다.
>




# **Help people choose useful names**
> 사용자가 유용한 이름을 선택할 수 있도록 도와줍니다
>




**Suggest service names that suit your accessory.** If your app detects that the user has created a suboptimal name for Siri voice controls, recommend alternatives that you know will work well for most people. Never suggest company names or model numbers for use as service names.
> 당신의 액세서리에 맞는 서비스 이름을 제안하세요. 만약 당신의 앱이 사용자가 Siri 음성 컨트롤을 위한 차선의 이름을 만든 것을 감지한다면, 대부분의 사람들에게 잘 작동할 것이라는 것을 알고 있는 대안을 추천하세요. 서비스 이름으로 사용할 회사 이름이나 모델 번호를 제안하지 마십시오.
>




**Check that user-provided names follow HomeKit naming rules.** If your app lets people rename services, make sure that the new names follow the rules. (The system-provided setup flow automatically checks the original names.) If people enter a name that breaks one or more rules, briefly explain the problem and suggest some alternative names that work. Here are the rules:
> 사용자가 제공한 이름이 HomeKit 이름 지정 규칙을 따르는지 확인하십시오. 앱에서 사용자가 서비스 이름을 변경할 수 있도록 허용하는 경우 새 이름이 규칙을 따르는지 확인하십시오. (시스템에서 제공하는 설정 흐름은 자동으로 원래 이름을 확인합니다.) 사용자가 하나 이상의 규칙을 위반하는 이름을 입력하는 경우 문제를 간단히 설명하고 사용할 수 있는 몇 가지 대체 이름을 제안합니다. 규칙은 다음과 같습니다:
>




- Use only alphanumeric, space, and apostrophe characters.
- >  영숫자, 공백 및 아포스트로피 문자만 사용하십시오.

- Start and end with an alphabetic or numeric character.
- >  알파벳 또는 숫자 문자로 시작하고 끝냅니다.

- Don't include emojis.

[제목 없음](https://www.notion.so/68e813d76fe24a30a363bc385014cf0c)

**Help people avoid creating names that include location information.** It’s natural for someone to use “kitchen light” to name a light in the kitchen, but including the room name in the service name can lead to unpredictable results when controlling the accessory by voice. Your app should detect service names that duplicate location information and help people fix them. For example, you might present a post-setup experience that removes the room or zone from a service name and encourages people to assign the accessory to that room or zone instead.
> 위치 정보가 포함된 이름을 만드는 것을 피할 수 있도록 도와줍니다. 누군가가 부엌에서 조명 이름을 짓는 데 "주방 조명"을 사용하는 것은 당연하지만, 서비스 이름에 룸 이름을 포함하면 음성으로 액세서리를 제어할 때 예측할 수 없는 결과를 초래할 수 있습니다. 당신의 앱은 위치 정보를 복제하는 서비스 이름을 감지하고 사람들이 그것을 고치는 것을 도와야 한다. 예를 들어, 서비스 이름에서 룸 또는 영역을 제거하고 대신 사용자가 해당 룸 또는 영역에 부속품을 할당하도록 하는 설정 후 환경을 제공할 수 있습니다.
>



