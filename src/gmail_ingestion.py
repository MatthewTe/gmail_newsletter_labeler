
class GmailPipeline(object):

    def __init__(self, **kwargs):
        """
        """
        self.message_ids = []        
        

    def authenticate_gmail_conn(self):
        """
        """
        self.gmail_authentication_service = None

    def connect_to_storage_bucket(self):
        """
        """
        self.minio_client = None

    def get_daily_newsletters(self):
        """
        """
        pass

    def parse_gmail_response(self):
        """
        """
        pass

    def store_newsletter_in_bucket(self):
        """
        """
        pass