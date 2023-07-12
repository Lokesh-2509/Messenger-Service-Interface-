from abc import ABC, abstractmethod
class MessagingService(ABC):
    @abstractmethod
    def sendMessage(self, message):
        pass
class SMSMessagingService(MessagingService):
    def sendMessage(self, message):
        print("Sending SMS:", message)
class EmailMessagingService(MessagingService):
    def sendMessage(self, message):
        print("Sending email:", message)
class WhatsAppMessagingService(MessagingService):
    def sendMessage(self, message):
        print("Sending WhatsApp message:", message)
sms_service = SMSMessagingService()
email_service = EmailMessagingService()
whatsapp_service = WhatsAppMessagingService()
sms_service.sendMessage("Hello, I am lokesh.")
email_service.sendMessage("Hello, this is an email.")
whatsapp_service.sendMessage("Hello, Regarding the examination.")
