# **[technologies-homekit] terminology-and-layout**

HomeKit models the home as a hierarchy of objects and defines a vocabulary of terms that refer to them. The Home app uses the HomeKit object model and terminology to give people intuitive control of accessories by voice, app, and automation.

It's crucial for your app to use the terminology and object model that HomeKit defines, so that you can reinforce people's understanding and make home automation feel approachable.

# **Homes**

HomeKit uses the term *home* to represent a physical home, office, or other location of relevance to the user. One user can have multiple homes.

![https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/hype/homekit/homeOne.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/hype/homekit/homeOne.svg)

Home

![https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/hype/homekit/office.svg](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/hype/homekit/office.svg)

Office

# **Rooms**

A *room* represents a physical room in a home. Rooms don’t have attributes like size or location; they’re simply names that have meaning to people, such as *Bedroom* or *Office*. When people assign accessories to a room, they can use voice commands like “Siri, turn on all the lights except the bedroom,” or "Siri, turn on the kitchen and hallway lights."

# **Accessories, services, and characteristics**

The term *accessory* represents a physical, connected home accessory, like a ceiling fan, lamp, lock, or camera. HomeKit uses *category* to represent a type of accessory, such as thermostat, fan, or light. Typically, an accessory manufacturer assigns each accessory to a category, but your app can help users make this assignment if necessary. For example, a switch that's connected to a fan or a lamp should be assigned to the same category as the accessory it controls.

A controllable feature of an accessory, such as the switch on a connected light, is known as a *service*. Some accessories offer multiple services. For example, a connected garage door might let people control the light and the door separately, or a connected outlet might support separate control of the top outlet and the bottom outlet. Apps don't use the word *service* in the UI; instead, they use names that describe the service, such as *garage door opener* and *ceiling fan light*. When people use Siri to control the accessories in their homes, they speak the service name, not the accessory name. For more guidance on naming, see [Help people choose useful names](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/setup#help-people-choose-useful-names).

A *characteristic* is a controllable attribute of a service. For example, in a ceiling fan, the fan service might have a speed characteristic and the light service might have a brightness characteristic. Apps don't use the word *characteristic* in the UI; instead, they use terms that describe the attribute, such as *speed* and *brightness*.

A *service group* represents a group of accessory services that a user might want to control as a unit. For example, a user could control the floor lamp and two table lamps in one corner of the living room by assigning all three services to a service group named *reading lamps*. Using the *reading lamps*service group, the user could control these three lights independently of all other lights in the living room.

# **Actions and scenes**

The term *action* refers to the changing of a service's characteristic, such as adjusting the speed of a fan or the brightness of a light. Actions are initiated by users and through automation.

A *scene* is a group of actions that control one or more services in one or more accessories. For example, a user might create a *Movie Time* scene that lowers the shades and dims the lights in the living room, or a *Good Morning* scene that turns on the lights, raises the shades, and starts the coffee maker in the kitchen.

**TIP**The HomeKit API uses the term *action set* instead of *scene*. In your app’s UI, always use the term *scene*.

# **Automations**

*Automations* cause accessories to react to certain situations, such as when the user’s location changes, a particular time of day occurs, another accessory turns on or off, or a sensor detects something. For example, an automation could turn on the house lights at sunset or when the user arrives home.

# **Zones**

A *zone* represents an area in the home that contains multiple rooms, such as *upstairs* or *downstairs*. Setting up a zone is optional, but doing so lets people control multiple accessories at one time. For example, assigning all downstairs lights to a zone named *downstairs* lets people use voice commands like “Siri, turn off all the lights downstairs.”

# **Home layout**

In the HomeKit model, the [home](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/terminology-and-layout#homes) object is the root of a hierarchy that contains all other objects, such as [rooms](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/terminology-and-layout#rooms), [accessories](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/terminology-and-layout#accessories-services-and-characteristics), and  [zones](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/terminology-and-layout#zones). If a user has more than one home, each home is the root of a different hierarchy.

**Acknowledge the hierarchical model that HomeKit uses.** Even if your app doesn’t organize accessories by rooms and zones in its UI, you should reference the HomeKit model when helping people set up or control their accessories. People need to know where accessories are located so they can use Siri and HomePod to control them by speaking commands like “Siri, turn on the lights upstairs,” or “It’s dark in here.” For more guidance, see [Siri interactions](https://developer.apple.com/design/human-interface-guidelines/technologies/homekit/siri-interactions).

**Make it easy for people to find an accessory’s related HomeKit details.** If your app's organization focuses on accessories, don’t hide other HomeKit information, such as an accessory’s zone or room, in a hard-to-discover settings screen. Instead, consider making the related HomeKit information easily available in an accessory detail view.

**Recognize that a user can have more than one home.** Even if your app doesn’t support the concept of multiple homes per user, consider providing the relevant home information in an accessory detail view.

**Don’t present duplicate home settings.** If your app has a different perspective on the organization of a home, don’t confuse people by asking them to set up all or parts of their homes again or by showing a duplicate settings view. Always defer to the settings people made in the Home app and find an intuitive way to present these details in your UI.