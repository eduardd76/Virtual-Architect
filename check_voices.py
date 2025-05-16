from elevenlabs import set_api_key, voices

set_api_key("sk_a1b8ce3b2047e14d0bfc55d5e7dcb1a6b239a9d217f2be11")  # cheia ta

available_voices = voices()
print("\n✅ Voicelist activ în contul tău:\n")
for v in available_voices:
    print(f"- {v.name}")
