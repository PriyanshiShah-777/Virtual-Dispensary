



# Initialize recognizer class (for recognizing the speech)

# r = sr.Recognizer()
#
# # Reading Microphone as source
# # listening the speech and store in audio_text variable
#
# with sr.Microphone() as source:
#     print("Talk")
#     audio_text = r.listen(source)
#     print("Time over, thanks")
#     # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
#
#     try:
#         # using google speech recognition
#         print("Text: " + r.recognize_google(audio_text))
#     except:
#         print("Sorry, I did not get that")
keyid = 'rzp_test_4CGtBNus2qEYSm'
keySecret = 'pl9DohUVb7nA9w3Tyx7CxCBZ'
import razorpay
client = razorpay.Client(auth=(keyid, keySecret))

medicine_price = 500


data = {
    'amount': medicine_price*100,
    "currency": "INR",
    "receipt": "Feelfreetocode123",
    "notes": {
        "name": "",
        "payment_for": "Doctor Fees"
    }
}



order1 = client.order.create(data=data)
print(order1)

print(order1['id'])

order_id = order1['id']




