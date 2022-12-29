# **[inputs] gyro-and-accelerometer**

## On-device gyroscopes and accelerometers can supply data about a device's movement in the physical world.
> 장치 내 자이로스코프와 가속도계는 물리적 세계에서 장치의 움직임에 대한 데이터를 제공할 수 있다.
>




![https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-gyroscope-intro_2x.png](https://developer.apple.com/design/human-interface-guidelines/images/intro/inputs/input-gyroscope-intro_2x.png)

You can use accelerometer and gyroscope data to enable experiences based on real-time, motion-based information in apps and games that run in iOS, iPadOS, and watchOS. tvOS apps can use gyroscope data from the Siri Remote. For developer guidance, see [Core Motion](https://developer.apple.com/documentation/coremotion).
> 가속도계와 자이로스코프 데이터를 사용하여 iOS, iPadOS 및 watchOS에서 실행되는 앱과 게임에서 실시간 모션 기반 정보를 기반으로 경험을 가능하게 할 수 있습니다. tvOS 앱은 시리 리모컨의 자이로스코프 데이터를 사용할 수 있습니다. 개발자 지침은 코어 모션을 참조하십시오.
>




# **Best practices**

**Use motion data only to offer a tangible benefit to people.** For example, a fitness app might use the data to provide feedback about people’s activity and general health, and a game might use the data to enhance gameplay. Avoid gathering data simply to have the data.
> 예를 들어 피트니스 앱은 사람들의 활동과 일반적인 건강에 대한 피드백을 제공하기 위해 데이터를 사용할 수 있고 게임은 게임플레이를 향상시키기 위해 데이터를 사용할 수 있다. 단순히 데이터를 얻기 위해 데이터를 수집하지 마십시오.
>




**IMPORTANT**If your experience needs to access motion data from a device, you must provide copy that explains why. The first time your app or game tries to access this type of data, the system includes your copy in a permission request, where people can grant or deny access.
> 중요 장치에서 모션 데이터에 액세스해야 하는 경우 그 이유를 설명하는 복사본을 제공해야 합니다. 앱이나 게임에서 처음으로 이러한 유형의 데이터에 액세스하려고 하면 시스템은 사용자의 복사본을 권한 요청에 포함하여 사용자가 액세스를 허용하거나 거부할 수 있습니다.
>




**Outside of active gameplay, avoid using accelerometers or gyroscopes for the direct manipulation of your interface.** Some motion-based gestures may be difficult to replicate precisely, may be physically challenging for some people to perform, and may affect battery usage.
> 일부 모션 기반 제스처는 정확하게 복제하기 어렵고 일부 사용자가 수행하기에 물리적으로 어려울 수 있으며 배터리 사용에 영향을 미칠 수 있습니다.
>




# **Platform considerations**

*No additional considerations for iOS, iPadOS, macOS, tvOS, or watchOS.*
> iOS, iPadOS, macOS, tvOS 또는 시계에 대한 추가 고려 사항 없음운영 체제
>



