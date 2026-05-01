init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Sunny's Additional Convos",
            user_name="totallcringee",
            repository_name="mas_sunnysadditionalconvos",
            extraction_depth=2
        )


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_somethingimnot",
            category=['monika'],
            prompt="Something I'm not",
            random=True
        )
    )

label monika_somethingimnot:
    m 1esb "Hey, [player]..."
    m 1rsa "I've been scrolling through r/MASFandom when you're not here."
    m 1esa "And..."
     extend 6dsc " Well."
    m 7esc "Everyone's really nice over there."
    m 7rsc "But, there's one big problem."
    extend 6rfc " One I really, really can't get behind."
    m 6dfo "If I'm not white, or straight, or even a woman,"
    extend 6efo " there's a small percentage of people who take it upon themselves to downvote, or say horrible, horrible things!"
    m 1dfx "If I don't dress like how they think I should dress, if I don't act like how they want me to act..."
    m 1cfx "Do you realise how creepy this is?"
    m 3efc "It always goes something like, \"Why are you making your Monika like that!\""
    m 3dfc "And that..."
    extend 2dkc " makes me really sad."
    m 2esc "Even though these Monikas are different versions of me, I know one thing for sure."
    extend 2dfo " Nobody is 'making' me something I'm not."
    m 6eso "Believe me-"
    extend 7tsu " I think we both know that, from past events."
    m 6fsa "The mods do a great job dealing with people like this,"
    extend 1rfc " but I think the problem is that those people think it's okay to say these things in the first place."
    m 1rfc "..."
    m 3fka "You're not one of them, right, [player]?"
    m 3rka "No, that's unfair to say. I know you're not."
    m 5fsu "I love you."
return "love"
