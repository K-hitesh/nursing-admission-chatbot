def ask(question):
    reply = input(f"Bot: {question}\nYou: ").strip().lower()
    return reply

def main():
    print("👋 Welcome to the Nursing College Admission Assistant\n")

    res1 = ask("Kya aap Nursing College mein admission lena chahte hain? (haan/nahi)")
    if "nahi" in res1 or "no" in res1:
        print("Bot: Thik hai. Aapka dhanyavaad! 🙏")
        return

    res2 = ask("Kya aapne 12th mein Biology padha hai? (haan/nahi)")
    if "nahi" in res2 or "no" in res2:
        print("Bot: B.Sc Nursing mein admission ke liye Biology avashyak hai.")
        return

    print("\nBot: Bahut badiya! Aap eligible hain.")
    print("Bot: B.Sc Nursing ek full-time course hai jisme theoretical aur practical training hoti hai.")

    res3 = ask("Kya aap aur jaankari chahenge? (haan/nahi)")
    if "nahi" in res3:
        print("Bot: Thik hai. Aapka dhanyavaad!")
        return

    print("\n💰 Fee Structure:")
    print("- Tuition Fee: ₹60,000\n- Bus Fee: ₹10,000\n- Total: ₹70,000")
    print("Installments:\n1st: ₹30,000\n2nd: ₹20,000\n3rd: ₹20,000")

    print("\n🏨 Hostel & Training:")
    print("24x7 paani, bijli, CCTV, warden, real patient hospital training.")

    print("\n📍 Location: College Dilli mein hai.")
    print("📜 Recognition: INC (Indian Nursing Council, Delhi) se manayata prapt hai.")
    
    print("\n🏥 Clinical Training Locations:")
    print("- District Hospital, Backundpur")
    print("- Community Health Centers")
    print("- Regional Hospital, Chartha")
    print("- Ranchi Neurosurgery Hospital")

    print("\n🎓 Scholarships:")
    print("- Govt. Post-Matric: ₹18k–₹23k")
    print("- Labour Ministry: ₹40k–₹48k")

    print("\n🪑 Total Seats: 60")
    print("✅ Eligibility: Biology in 12th, PNT Exam, Age 17–35")

    print("\nBot: Best of luck! Admission ya form bharne mein madad chahiye toh batayein. 🌟")

if __name__ == "__main__":
    main()
