# **[technologies-homekit] terminology-and-layout**

HomeKit models the home as a hierarchy of objects and defines a vocabulary of terms that refer to them. The Home app uses the HomeKit object model and terminology to give people intuitive control of accessories by voice, app, and automation.
> 홈킷은 객체의 계층 구조로 가정을 모델링하고 이를 가리키는 용어의 어휘를 정의한다. 홈 앱은 홈킷 객체 모델과 용어를 사용하여 사람들에게 음성, 앱 및 자동화에 의한 액세서리에 대한 직관적인 제어를 제공한다.
>




It's crucial for your app to use the terminology and object model that HomeKit defines, so that you can reinforce people's understanding and make home automation feel approachable.
> 당신의 앱은 HomeKit가 정의하는 용어와 객체 모델을 사용하여 사람들의 이해를 강화하고 홈 오토메이션이 접근 가능하다고 느낄 수 있도록 하는 것이 중요하다.
>




# **Homes**

HomeKit uses the term *home* to represent a physical home, office, or other location of relevance to the user. One user can have multiple homes.
> 홈킷(HomeKit)은 사용자와 관련된 물리적인 집, 사무실 또는 기타 위치를 나타내는 용어이다. 한 사용자가 여러 집을 가질 수 있습니다.
>




![https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/hype/homekit/homeOne.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/hype/homekit/homeOne.svg)

Home

![https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/hype/homekit/office.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/hype/homekit/office.svg)

Office

# **Rooms**

A *room* represents a physical room in a home. Rooms don’t have attributes like size or location; they’re simply names that have meaning to people, such as *Bedroom* or *Office*. When people assign accessories to a room, they can use voice commands like “Siri, turn on all the lights except the bedroom,” or "Siri, turn on the kitchen and hallway lights."
> 방은 가정의 물리적인 방을 나타냅니다. 룸에는 크기나 위치와 같은 속성이 없으며, 침실이나 사무실과 같이 단순히 사람에게 의미가 있는 이름입니다. 사람들이 방에 액세서리를 할당할 때, 그들은 "시리, 침실을 제외한 모든 불을 켜라" 또는 "시리, 부엌과 복도의 불을 켜라"와 같은 음성 명령을 사용할 수 있다
>




# **Accessories, services, and characteristics**

The term *accessory* represents a physical, connected home accessory, like a ceiling fan, lamp, lock, or camera. HomeKit uses *category* to represent a type of accessory, such as thermostat, fan, or light. Typically, an accessory manufacturer assigns each accessory to a category, but your app can help users make this assignment if necessary. For example, a switch that's connected to a fan or a lamp should be assigned to the same category as the accessory it controls.
> 액세서리라는 용어는 천장 팬, 램프, 잠금 장치 또는 카메라와 같은 물리적으로 연결된 홈 액세서리를 나타냅니다. HomeKit는 카테고리를 사용하여 서모스탯, 팬 또는 조명과 같은 액세서리 유형을 나타냅니다. 일반적으로 액세서리 제조업체는 각 액세서리를 범주에 할당하지만 필요한 경우 앱을 통해 사용자가 이 할당을 수행할 수 있습니다. 예를 들어, 팬 또는 램프에 연결된 스위치는 제어하는 부속품과 동일한 범주에 할당되어야 합니다.
>




A controllable feature of an accessory, such as the switch on a connected light, is known as a *service*. Some accessories offer multiple services. For example, a connected garage door might let people control the light and the door separately, or a connected outlet might support separate control of the top outlet and the bottom outlet. Apps don't use the word *service* in the UI; instead, they use names that describe the service, such as *garage door opener* and *ceiling fan light*. When people use Siri to control the accessories in their homes, they speak the service name, not the accessory name. For more guidance on naming, see [Help people choose useful names](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/setup#help-people-choose-useful-names).
> 연결된 조명의 스위치와 같은 액세서리의 제어 가능한 기능을 서비스라고 합니다. 일부 액세서리는 여러 서비스를 제공합니다. 예를 들어, 연결된 차고 문은 사람들이 조명과 문을 별도로 제어할 수 있도록 하거나, 연결된 콘센트는 상단 콘센트와 하단 콘센트의 별도 제어를 지원할 수 있다. 앱들은 UI에서 서비스라는 단어를 사용하지 않고 대신 차고 문 개폐기와 천장 선풍기 조명과 같은 서비스를 설명하는 이름을 사용한다. 사람들이 집에 있는 액세서리를 제어하기 위해 시리를 사용할 때, 그들은 액세서리 이름이 아닌 서비스 이름을 말합니다. 이름 지정에 대한 자세한 내용은 사용자가 유용한 이름을 선택하는 데 도움을 참조하십시오.
>




A *characteristic* is a controllable attribute of a service. For example, in a ceiling fan, the fan service might have a speed characteristic and the light service might have a brightness characteristic. Apps don't use the word *characteristic* in the UI; instead, they use terms that describe the attribute, such as *speed* and *brightness*.
> 특성은 서비스의 제어 가능한 속성입니다. 예를 들어, 천장 팬에서 팬 서비스는 속도 특성을 가질 수 있고 라이트 서비스는 밝기 특성을 가질 수 있다. 앱은 UI에서 특성이라는 단어를 사용하지 않고 속도 및 밝기와 같은 속성을 설명하는 용어를 사용합니다.
>




A *service group* represents a group of accessory services that a user might want to control as a unit. For example, a user could control the floor lamp and two table lamps in one corner of the living room by assigning all three services to a service group named *reading lamps*. Using the *reading lamps*service group, the user could control these three lights independently of all other lights in the living room.
> 서비스 그룹은 사용자가 하나의 단위로 제어하고자 하는 액세서리 서비스 그룹을 나타냅니다. 예를 들어, 사용자는 독서등이라는 서비스 그룹에 세 가지 서비스를 모두 할당하여 거실 한쪽 구석에 있는 플로어 램프와 두 개의 테이블 램프를 제어할 수 있다. 사용자는 독서등 서비스 그룹을 사용하여 거실의 다른 모든 조명과 독립적으로 이 세 개의 조명을 제어할 수 있었다.
>




# **Actions and scenes**

The term *action* refers to the changing of a service's characteristic, such as adjusting the speed of a fan or the brightness of a light. Actions are initiated by users and through automation.
> 조치라는 용어는 선풍기의 속도나 조명의 밝기를 조절하는 것과 같은 서비스의 특성을 변화시키는 것을 말한다. 작업은 사용자와 자동화를 통해 시작됩니다.
>




A *scene* is a group of actions that control one or more services in one or more accessories. For example, a user might create a *Movie Time* scene that lowers the shades and dims the lights in the living room, or a *Good Morning* scene that turns on the lights, raises the shades, and starts the coffee maker in the kitchen.
> 장면은 하나 이상의 부속품에서 하나 이상의 서비스를 제어하는 작업 그룹입니다. 예를 들어 사용자는 거실의 차양을 낮추고 조명을 어둡게 하는 Movie Time 장면이나 조명을 켜고 차양을 올린 다음 부엌에서 커피메이커를 시작하는 Good Morning 장면을 만들 수 있습니다.
>




**TIP**The HomeKit API uses the term *action set* instead of *scene*. In your app’s UI, always use the term *scene*.
> TIPT HomeKit API는 장면 대신 액션 세트라는 용어를 사용합니다. 앱 UI에서 항상 씬(scene)이라는 용어를 사용합니다.
>




# **Automations**

*Automations* cause accessories to react to certain situations, such as when the user’s location changes, a particular time of day occurs, another accessory turns on or off, or a sensor detects something. For example, an automation could turn on the house lights at sunset or when the user arrives home.
> 자동화는 사용자의 위치가 변경되거나, 하루 중 특정 시간이 발생하거나, 다른 액세서리가 켜지거나 꺼지거나, 센서가 무언가를 감지하는 등의 특정 상황에 액세서리가 반응하도록 합니다. 예를 들어, 자동화는 해가 질 때나 사용자가 집에 도착할 때 집 조명을 켤 수 있다.
>




# **Zones**

A *zone* represents an area in the home that contains multiple rooms, such as *upstairs* or *downstairs*. Setting up a zone is optional, but doing so lets people control multiple accessories at one time. For example, assigning all downstairs lights to a zone named *downstairs* lets people use voice commands like “Siri, turn off all the lights downstairs.”
> 영역은 위층 또는 아래층과 같이 여러 개의 룸을 포함하는 집의 영역을 나타냅니다. 영역 설정은 선택 사항이지만 이렇게 하면 사용자가 한 번에 여러 부속품을 제어할 수 있습니다. 예를 들어, 모든 아래층 조명을 아래층이라는 이름의 구역에 할당하는 것은 사람들이 "시리, 아래층의 모든 조명을 꺼라"와 같은 음성 명령을 사용할 수 있게 한다
>




# **Home layout**

In the HomeKit model, the [home](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/terminology-and-layout#homes) object is the root of a hierarchy that contains all other objects, such as [rooms](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/terminology-and-layout#rooms), [accessories](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/terminology-and-layout#accessories-services-and-characteristics), and  [zones](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/terminology-and-layout#zones). If a user has more than one home, each home is the root of a different hierarchy.
> HomeKit 모델에서 홈 객체는 룸, 부속품 및 구역과 같은 다른 모든 객체를 포함하는 계층의 루트입니다. 사용자가 둘 이상의 홈을 가지고 있는 경우 각 홈은 서로 다른 계층의 루트입니다.
>




**Acknowledge the hierarchical model that HomeKit uses.** Even if your app doesn’t organize accessories by rooms and zones in its UI, you should reference the HomeKit model when helping people set up or control their accessories. People need to know where accessories are located so they can use Siri and HomePod to control them by speaking commands like “Siri, turn on the lights upstairs,” or “It’s dark in here.” For more guidance, see [Siri interactions](../technologies/homekit/siri-interactions).
> HomeKit이 사용하는 계층적 모델을 확인하십시오. 앱이 UI에서 룸 및 구역별로 액세서리를 구성하지 않더라도 사용자가 액세서리를 설정하거나 제어할 때 HomeKit 모델을 참조해야 합니다. 사람들은 액세서리가 어디에 있는지 알아야만 그들이 시리와 홈팟을 사용하여 "시리, 위층의 불을 켜라" 또는 "여기는 어둡다"와 같은 명령을 말함으로써 액세서리를 제어할 수 있다 자세한 내용은 Siri 상호작용을 참조하십시오.
>




**Make it easy for people to find an accessory’s related HomeKit details.** If your app's organization focuses on accessories, don’t hide other HomeKit information, such as an accessory’s zone or room, in a hard-to-discover settings screen. Instead, consider making the related HomeKit information easily available in an accessory detail view.
> 앱의 구성이 액세서리에 초점을 맞춘 경우 액세서리 구역이나 룸과 같은 다른 HomeKit 정보를 찾기 어려운 설정 화면에 숨기지 마십시오. 대신, 관련 HomeKit 정보를 액세서리 세부 정보 보기에서 쉽게 사용할 수 있도록 하는 것을 참조하십시오.
>




**Recognize that a user can have more than one home.** Even if your app doesn’t support the concept of multiple homes per user, consider providing the relevant home information in an accessory detail view.
> 한 사용자가 두 개 이상의 집을 가질 수 있음을 인식하십시오. 앱이 사용자당 여러 집이라는 개념을 지원하지 않더라도 관련 홈 정보를 액세서리 세부 정보 보기로 제공하는 것을 고려하십시오.
>




**Don’t present duplicate home settings.** If your app has a different perspective on the organization of a home, don’t confuse people by asking them to set up all or parts of their homes again or by showing a duplicate settings view. Always defer to the settings people made in the Home app and find an intuitive way to present these details in your UI.
> 홈 설정을 중복으로 표시하지 마십시오. 앱이 홈 구성에 대해 다른 관점을 가지고 있다면 홈의 전체 또는 일부를 다시 설정하도록 요청하거나 중복된 설정 보기를 표시하여 사람들을 혼란스럽게 하지 마십시오. 항상 홈 앱에서 사용자가 설정한 설정을 따르고 UI에서 이러한 세부 정보를 표시할 수 있는 직관적인 방법을 찾으십시오.
>



