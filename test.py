import unittest
from bnlp.sentencepiece_tokenizer import SP_Tokenizer
from bnlp.nltk_tokenizer import NLTK_Tokenizer
from bnlp.basic_tokenizer import BasicTokenizer
from bnlp.bengali_word2vec import Bengali_Word2Vec
from bnlp.bengali_fasttext import Bengali_Fasttext

class TestBNLP(unittest.TestCase):

    def test_BT(self):
        bt = BasicTokenizer(False)
        text = "আমি ভাত খাই।"
        tokens = bt.tokenize(text)
        self.assertEqual(tokens, ["আমি", "ভাত", "খাই", "।"])

        text1 = """
        ভারত থেকে অনুপ্রবেশ ঠেকাতে বর্ডার গার্ড বাংলাদেশের (বিজিবি)
         সঙ্গে রাজশাহীর চরখানপুর সীমান্ত পাহারা দিচ্ছেন গ্রামবাসী।
         সীমান্তে নজরদারি জোরদার করার জন্য     চরখানপুর গ্রামের প্রায় আড়াই শ 
         বাসিন্দা রাত জেগে পালাক্রমে এই কাজ করছেন গত ২৮ নভেম্বর থেকে।
        """
        tokens1 = bt.tokenize(text1)
        output_1 = ["ভারত", "থেকে", "অনুপ্রবেশ", "ঠেকাতে", "বর্ডার", "গার্ড", "বাংলাদেশের", "(", "বিজিবি", ")",
         "সঙ্গে", "রাজশাহীর", "চরখানপুর", "সীমান্ত", "পাহারা", "দিচ্ছেন", "গ্রামবাসী", "।",
         "সীমান্তে", "নজরদারি", "জোরদার", "করার", "জন্য", "চরখানপুর", "গ্রামের", "প্রায়", "আড়াই", "শ", 
         "বাসিন্দা", "রাত", "জেগে", "পালাক্রমে", "এই", "কাজ", "করছেন", "গত", "২৮", "নভেম্বর", "থেকে", "।"]
        self.assertEqual(tokens1, output_1)


    

if __name__ == '__main__':
    unittest.main()
