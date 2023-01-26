# **[technologies-homekit] custom-functionality**

Your app is a great place to help people appreciate the unique functionality of your accessory. For example, an app for a light that displays different colors could help people create HomeKit scenes using colors imported from their photos.
> 당신의 앱은 사람들이 당신의 액세서리의 독특한 기능을 이해하도록 돕는 좋은 장소이다. 예를 들어, 다른 색을 표시하는 조명용 앱은 사람들이 사진에서 가져온 색을 사용하여 홈킷 장면을 만드는 데 도움을 줄 수 있다.
>




**Be clear about what users can do in your app and when they should use the Home app.** For example, if your app supports only lights, you should consider encouraging people to create a "Movie Time" scene that not only dims the lights, but also closes the shades, and turns on the TV to a specific input. To do this, first guide people to set up a scene that includes only your accessory's actions—in this scenario, dimming the lights. Then, your app can suggest that people open the Home app to add their HomeKit-enabled shades and TV to the scene you helped them create. For guidance on how to refer to the Home app, see [Home app icon](https://developer.apple.com/design/human-interface-guidelines/homekit/overview/icons/#apple-home-app-icon) and [Editorial guidelines](../homekit/overview/editorial/).
> 예를 들어 앱에서 사용자가 할 수 있는 작업과 홈 앱을 사용해야 하는 시간을 명확히 해야 합니다. 예를 들어, 앱이 조명만 지원하는 경우 조명을 어둡게 할 뿐만 아니라 음영을 닫고 특정 입력으로 TV를 켜는 "Movie Time" 장면을 만들도록 권장하는 것을 고려해야 합니다. 이렇게 하려면 먼저 사람들에게 액세서리의 동작만 포함된 장면(이 시나리오에서는 조명을 어둡게 함)을 설정하도록 안내합니다. 그런 다음, 당신의 앱은 당신이 만든 장면에 홈킷 사용 가능한 색조와 TV를 추가하기 위해 사람들이 홈 앱을 열 것을 제안할 수 있다. 홈 앱을 참조하는 방법에 대한 지침은 홈 앱 아이콘 및 편집 지침을 참조하십시오.
>




**Defer to HomeKit if your database differs from the HomeKit database.** Give people a seamless experience by automatically reflecting changes made in the Home app or in other third-party HomeKit apps. If you must ask people to manage conflicts in your app, present the conflict visually so that they have a clear picture of the choice they need to confirm. For example, if the user changes an accessory's service name in the Home app, your app can detect this change and could show both names side by side to confirm that the user wants to use the new name in your app, too.
> 데이터베이스가 HomeKit 데이터베이스와 다른 경우 HomeKit를 사용하십시오. HomeKit 앱 또는 다른 타사 HomeKit 앱에서 변경된 내용을 자동으로 반영하여 사용자에게 원활한 환경을 제공합니다. 앱에서 충돌을 관리하도록 사용자에게 요청해야 하는 경우, 확인해야 할 선택 사항을 명확하게 표시할 수 있도록 충돌을 시각적으로 표시합니다. 예를 들어 사용자가 홈 앱에서 액세서리의 서비스 이름을 변경하면 앱에서 이 변경 사항을 감지하고 두 이름을 나란히 표시하여 사용자가 앱에서도 새 이름을 사용하려는 것을 확인할 수 있습니다.
>




**Ask permission to update the HomeKit database when users make changes in your app.**People should never be surprised by something that changes in the Home app, so it’s essential to get permission or an indication of intent before you write to the database. In particular, never overwrite HomeKit database settings without explicit direction from the user.
> 사용자가 앱을 변경할 때 HomeKit 데이터베이스를 업데이트할 수 있는 권한을 요청하십시오.홈 앱에서 변경되는 것에 사람들이 놀라지 않아야 하므로 데이터베이스에 쓰기 전에 허가를 받거나 의도를 나타내는 것이 필수적이다. 특히 사용자의 명시적인 지시 없이 HomeKit 데이터베이스 설정을 덮어쓰지 마십시오.
>




# **Cameras**

Your app can display still images or streaming video from a connected HomeKit IP camera.
> 연결된 HomeKit IP 카메라에서 정지 이미지 또는 스트리밍 비디오를 표시할 수 있습니다.
>




**Don't block camera imagery.** It's fine to supplement the camera's content with useful features, such as an alert calling attention to potentially interesting activity. However, you should avoid covering portions of the camera's imagery with other content.
> 카메라 이미지를 차단하지 마십시오. 카메라의 콘텐츠를 잠재적으로 흥미로운 활동에 주의를 환기시키는 경고와 같은 유용한 기능으로 보완하는 것이 좋습니다. 그러나 카메라 이미지의 일부를 다른 콘텐츠로 덮어두는 것은 피해야 합니다.
>




**Show a microphone button only if the camera supports bidirectional audio.** A non-functioning microphone button takes up valuable display space in your app and risks confusing people.
> 카메라가 양방향 오디오를 지원하는 경우에만 마이크로폰 버튼을 표시하십시오. 작동하지 않는 마이크로폰 버튼은 앱에서 귀중한 표시 공간을 차지하므로 사람들을 혼란스럽게 할 수 있습니다.
>



