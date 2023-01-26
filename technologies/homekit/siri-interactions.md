# **[technologies-homekit] siri-interactions**

HomeKit enables powerful, hands-free control using voice commands. You can help people use Siri to interact with accessories, services, and zones in their home quickly and efficiently.
> 홈킷은 음성 명령을 사용하여 강력하고 핸즈프리한 제어를 가능하게 한다. 당신은 사람들이 시리를 사용하여 가정에서 액세서리, 서비스 및 구역과 빠르고 효율적으로 상호 작용하도록 도울 수 있다.
>




**Present example voice commands to demonstrate using Siri to control accessories during setup.** As soon as people complete the setup of a new accessory, consider using the service name they chose in a few example Siri phrases and encourage people to try them out.
> 설정 중에 Siri를 사용하여 액세서리를 제어하는 것을 시연하는 음성 명령의 예를 제시합니다. 사람들이 새로운 액세서리의 설정을 완료하는 즉시 몇 가지 예시 Siri 문구에서 선택한 서비스 이름을 사용하는 것을 고려하고 사용자들이 사용해 보도록 권장합니다.
>




**After setup, consider teaching people about more complex Siri commands.** People might not be aware of the broad range of natural language phrases they can use with Siri and HomePod to control their accessories. After setup is complete, find useful places throughout your app to help people learn about these types of commands. For example, in a scene detail view, you could tell people, *You can say "Hey Siri, set 'Movie Time.'”*
> 설정 후에는 사람들에게 더 복잡한 Siri 명령어에 대해 가르치는 것을 고려해 보십시오. 사람들은 액세서리를 제어하기 위해 Siri 및 HomePod와 함께 사용할 수 있는 광범위한 자연어 구문에 대해 알지 못할 수 있습니다. 설정이 완료되면 앱 전체에서 유용한 위치를 찾아 이러한 유형의 명령을 배울 수 있습니다. 예를 들어, 장면 세부 보기에서 사람들에게 "안녕 시리, '영화 시간'을 설정해"라고 말할 수 있습니다
>




In addition to recognizing the names of homes, rooms, zones, services, and scenes, Siri can also use information such as accessory category and characteristic to identify a service. For example, when people use terms like *brighter* or *dim*, Siri recognizes that they're referring to a service that has a brightness characteristic, even if they don't speak the name of the service.
> 시리는 집, 방, 구역, 서비스, 장면 등의 이름을 인식하는 것 외에도 액세서리 카테고리, 특성 등의 정보를 활용해 서비스를 식별할 수 있다. 예를 들어, 사람들이 더 밝거나 희미한 용어를 사용할 때, 시리는 비록 그들이 서비스의 이름을 말하지 않더라도 밝기 특성을 가진 서비스를 가리키는 것이라고 인식한다.
>




To illustrate the power and flexibility of Siri commands, here are some examples of the types of phrases that people could use to control their accessories.
> 시리 명령의 힘과 유연성을 설명하기 위해, 여기 사람들이 액세서리를 제어하는 데 사용할 수 있는 문구 유형의 몇 가지 예가 있다.
>




| Phrase | Siri understands |
| --- | --- |
| "Turn on the floor lamp" | Service (floor lamp) |
| "Show me the entryway camera" | Service (entryway camera) |
| "Turn on the light" | Accessory category (light) |
| "Turn off the living room light" | Room (living room)Accessory category (light) |
| "Make the living room a little bit brighter" | Room (living room)Accessory category (implied)Brightness characteristic (brighter) |
| "Turn on the recessed lights" | Service group (recessed lights) |
| "Turn off the lights upstairs" | Accessory category (lights)Zone (upstairs) |
| "Dim the lights in the bedroom and nursery" | Accessory category (lights)Brightness characteristic (dim) Rooms (bedroom, nursery) |
| "Run Good night" | Scene (Good night) |
| "Is someone in the living room?" | Accessory category (implied)Occupancy detection characteristic (implied) |
| "Is my security system tripped?" | Accessory category (security system) |
| "Did I leave the garage door open?" | Accessory category (garage door)Open characteristic (open) |
| "Did I forget to turn off the lights in the Tahoe House?" | Accessory category (lights)Home (Tahoe House) |
| "It's dark in here" | Current home (here)Current room (via HomePod)Accessory category (implied) |

**Recommend that people create zones and service groups, if they make sense for your accessory.** If people might benefit from using context-specific voice commands to control your accessory, suggest these types of interactions and help people set them up. For example, if you provide an accessory such as a light, switch, or thermostat, you could suggest setting up a zone named "upstairs" or a service group named "media center" to enable commands like “Siri, turn off the upstairs lights,” or “Siri, activate the media center.”
> 액세서리를 제어하기 위해 상황별 음성 명령을 사용하여 사용자에게 도움이 될 수 있는 경우 이러한 유형의 상호 작용을 제안하고 사용자가 설정하는 데 도움을 줄 수 있습니다. 예를 들어 조명, 스위치 또는 서모스탯과 같은 액세서리를 제공하는 경우 "위층" 또는 "미디어 센터"라는 서비스 그룹을 설정하여 "시리, 위층 불을 끄십시오" 또는 "시리, 미디어 센터를 활성화하십시오"와 같은 명령을 사용하도록 제안할 수 있습니다
>




**Offer shortcuts only for accessory-specific functionality that HomeKit doesn’t support.**HomeKit lets people use ordinary (or natural) language to control accessories without requiring any additional configuration, so you shouldn't confuse people by offering shortcuts that duplicate HomeKit functionality. Instead, consider offering shortcuts for complementary functionality that your app provides. For example, if people often want to order filters for an air conditioner that you support, you might offer a shortcut like "Order AC filters." To learn how to provide phrases that people can use for shortcuts, see [Shortcuts and suggestions](../technologies/siri/shortcuts-and-suggestions).
> HomeKit에서 지원하지 않는 액세서리별 기능에 대해서만 바로 가기를 제공합니다.HomeKit는 사용자가 추가 구성 없이 일반(또는 자연) 언어를 사용하여 액세서리를 제어할 수 있도록 하므로 HomeKit 기능을 복제하는 바로 가기를 제공하여 사용자를 혼란스럽게 해서는 안 됩니다. 대신 앱이 제공하는 보완 기능을 위한 바로 가기를 제공하는 것을 고려해 보십시오. 예를 들어 사용자가 지원하는 에어컨 필터를 주문하려는 경우 "AC 필터 주문"과 같은 바로 가기를 제공할 수 있습니다 바로 가기에 사용할 수 있는 구문을 제공하는 방법에 대한 자세한 내용은 바로 가기 및 제안을 참조하십시오.
>




**If your app supports both HomeKit and shortcuts, help users understand the difference between these types of voice control.** People can get confused if they're presented with multiple methods of voice control. Be sure you clearly indicate what’s possible with shortcuts, and never encourage users to create a shortcut for a scene or action that HomeKit already supports.
> 앱이 HomeKit와 바로 가기를 모두 지원하는 경우 사용자가 이러한 유형의 음성 컨트롤 간의 차이를 이해할 수 있도록 도와줍니다. 여러 가지 음성 컨트롤 방법이 제공되면 사람들이 혼동할 수 있습니다. 바로 가기를 사용하여 무엇이 가능한지 명확히 표시해야 하며, 사용자가 HomeKit에서 이미 지원하는 장면이나 동작에 대한 바로 가기를 만들도록 권장하지 마십시오.
>



