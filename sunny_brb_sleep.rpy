init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="sunny_brb_sleep",
            category=["be right back"],
            prompt="I'm going to sleep, [m_name]",
            pool=True,
            unlocked=True,
        ),
        markSeen=True
    )

label sunny_brb_sleep:
    m 1wuo "Ah, is it that late already?"
    m 1fka "Okay. {w=0.4}{nw}"
    extend 3hua "I'll watch over you while you sleep, [player]. {w=0.2}{nw}"
    extend 3eua " Sweet dreams."
    m 1fkbsa "I love you."

$ mas_idle_mailbox.send_idle_cb("sunny_brb_sleep_callback")
return "idle"

label sunny_brb_sleep_callback:
        m 1eub "You're back, [player]!{w=0.4}{nw}"
        extend 1fua " Did you sleep well?"
        m 3hua "Feel free to take a nap later if you still don't feel fully rested!"
return
