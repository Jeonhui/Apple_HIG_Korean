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




