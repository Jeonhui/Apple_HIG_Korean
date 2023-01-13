# **[technologies-homekit] siri-interactions**

HomeKit enables powerful, hands-free control using voice commands. You can help people use Siri to interact with accessories, services, and zones in their home quickly and efficiently.

**Present example voice commands to demonstrate using Siri to control accessories during setup.** As soon as people complete the setup of a new accessory, consider using the service name they chose in a few example Siri phrases and encourage people to try them out.

**After setup, consider teaching people about more complex Siri commands.** People might not be aware of the broad range of natural language phrases they can use with Siri and HomePod to control their accessories. After setup is complete, find useful places throughout your app to help people learn about these types of commands. For example, in a scene detail view, you could tell people, *You can say "Hey Siri, set 'Movie Time.'”*

In addition to recognizing the names of homes, rooms, zones, services, and scenes, Siri can also use information such as accessory category and characteristic to identify a service. For example, when people use terms like *brighter* or *dim*, Siri recognizes that they're referring to a service that has a brightness characteristic, even if they don't speak the name of the service.

To illustrate the power and flexibility of Siri commands, here are some examples of the types of phrases that people could use to control their accessories.

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

**Offer shortcuts only for accessory-specific functionality that HomeKit doesn’t support.**HomeKit lets people use ordinary (or natural) language to control accessories without requiring any additional configuration, so you shouldn't confuse people by offering shortcuts that duplicate HomeKit functionality. Instead, consider offering shortcuts for complementary functionality that your app provides. For example, if people often want to order filters for an air conditioner that you support, you might offer a shortcut like "Order AC filters." To learn how to provide phrases that people can use for shortcuts, see [Shortcuts and suggestions](https://developer.apple.com/design/human-interface-guidelines/technologies/siri/shortcuts-and-suggestions).

**If your app supports both HomeKit and shortcuts, help users understand the difference between these types of voice control.** People can get confused if they're presented with multiple methods of voice control. Be sure you clearly indicate what’s possible with shortcuts, and never encourage users to create a shortcut for a scene or action that HomeKit already supports.