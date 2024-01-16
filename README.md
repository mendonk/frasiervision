# README

FrasierVision leverages the power of AI to write single scenes of the television show Frasier, limited only by your imagination!

Available in Python and as a Docker image.

## Usage

There are three steps to FrasierVision:

1. `script_scraper.py` scrapes 3 PDF scripts from a website to a `/pdfs` folder.

2. `script_loader.py` loads PDF files in `/pdfs` into an Astra vector database.

3. `script_chat.py` prompts the vector database and returns a 1-scene script of the television program.

If you're very busy and you want to run all 3 steps at once, run `python3 frasiervision.py`. If you get `ValueError: [{"message": "Query timed out after PT30S"}]` run the program again and it *should* work.

Alternatively, run only the steps you need:

1. Run `script_scraper.py` only once to scrape the PDFs.

2. Run `script_loader.py` only once to populate the database.

3. After that, the "brain" of the application is generated. You can then repeatedly run `script_chat.py` and alter the question in `response = chain.invoke` to generate different scenes.

## Prerequisites

You need an Astra vector database. Create one at astra.datastax.com.

You need an open-ai API key.

Put the openai key, Astra endpoint, and Astra token in a .env file. (An example .env is provided.)

The following packages:
```
pip install ragstack-ai, python-dotenv, pypdf
```

## Example run

With `response = chain.invoke("What would happen if Frasier left KACL to work at OpenAI?")`

`python3 frasiervision.py`

```
Scene: KACL Radio Station - Roz's Booth

Roz is sitting in her booth, screening calls for The Frasier Crane Show. She looks bored and disinterested, clearly longing for something more stimulating in her career. Suddenly, her phone rings, and she picks it up.

Roz: (sighs) KACL, Roz Doyle speaking. How can I help you?

Caller: (v.o.) Hi Roz, it's Simon from OpenAI. I hope you're doing well.

Roz's eyes widen with excitement, realizing who is on the other end of the line.

Roz: Simon! It's so great to hear from you. What can I do for you?

Simon: Well, Roz, we've been following your work at KACL, and we think you'd be a perfect fit for OpenAI. We're impressed with your ability to handle the calls and your deep understanding of the show's dynamics.

Roz's face lights up, a mix of surprise and excitement.

Roz: OpenAI? Are you serious? That's incredible! I've always been fascinated by artificial intelligence and the possibilities it holds. Tell me more.

Simon: We're expanding our team of screenwriters, and we believe your expertise and knowledge of the characters would be invaluable. We want you to join us in creating compelling and realistic dialogues for our AI models.

Roz: (grinning) This is a dream come true. I've always wanted to explore new opportunities in my career, and working with OpenAI sounds like an amazing adventure. When can I start?

Simon: We'd love to have you onboard as soon as possible. We'll send over the details and contracts for you to review. Once everything is settled, we'll arrange for your transition from KACL to OpenAI.

Roz: Thank you so much, Simon. I can't wait to embark on this new chapter. It's going to be incredible.

Simon: We're thrilled to have you, Roz. Get ready for an exciting journey with OpenAI.

Roz hangs up the phone and takes a moment to absorb the news. She looks around the booth, feeling a mix of nostalgia and anticipation for what lies ahead. With a determined smile, she starts packing up her belongings, ready to begin her adventure with OpenAI.
```

## Run in Docker

1. Run `docker build -t frasiervision .` to create a Docker image from the Dockerfile.
2. Export your values from .env to your shell:
```
export ASTRA_DB_APPLICATION_TOKEN=AstraCS:...
export OPENAI_API_KEY=sk-...
export ASTRA_DB_API_ENDPOINT=https://<DB-ID>-<REGION>.apps.astra.datastax.com
export ASTRA_DB_COLLECTION=test
```

3. Start and run the container with the exported variables:
```
docker run -e ASTRA_DB_APPLICATION_TOKEN=$ASTRA_DB_APPLICATION_TOKEN \
           -e OPENAI_API_KEY=$OPENAI_API_KEY \
           -e ASTRA_DB_API_ENDPOINT=$ASTRA_DB_API_ENDPOINT \
           -e ASTRA_DB_COLLECTION=$ASTRA_DB_COLLECTION \
           frasiervision
```

4. Example build:
```
(fv) ➜  example docker build -t frasiervision
[+] Building 1.5s (12/12) FINISHED 0.0s

...

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
```

5. Example docker run:
```
(fv) ➜  example docker run -e ASTRA_DB_APPLICATION_TOKEN=$ASTRA_DB_APPLICATION_TOKEN \
           -e OPENAI_API_KEY=$OPENAI_API_KEY \
           -e ASTRA_DB_API_ENDPOINT=$ASTRA_DB_API_ENDPOINT \
           -e ASTRA_DB_COLLECTION=$ASTRA_DB_COLLECTION \
           frasiervision

/usr/local/lib/python3.9/site-packages/langchain_core/_api/deprecation.py:117: LangChainDeprecationWarning: The class `langchain_community.embeddings.openai.OpenAIEmbeddings` was deprecated in langchain-community 0.1.0 and will be removed in 0.2.0. Use langchain_openai.OpenAIEmbeddings instead.
  warn_deprecated(
/usr/local/lib/python3.9/site-packages/langchain_core/_api/deprecation.py:117: LangChainDeprecationWarning: The class `langchain_community.chat_models.openai.ChatOpenAI` was deprecated in langchain-community 0.1.0 and will be removed in 0.2.0. Use langchain_openai.ChatOpenAI instead.
  warn_deprecated(
Directory './pdfs' created
INT. KACL RADIO STATION - DAY

Frasier is wrapping up his radio show, talking to Roz in the control booth.

Frasier: Well, Roz, another successful show in the books. I must say, I do enjoy helping people with their problems.

Roz: You've got a real talent for it, Frasier. But hey, speaking of helping people, have you heard about this new company called OpenAI? They're doing some groundbreaking work in artificial intelligence.

Frasier: OpenAI? Yes, I've heard of them. They're at the forefront of innovation in the tech world. What about them?

Roz: Well, rumor has it they're looking for someone with your expertise to join their team. Can you imagine, Frasier? Using your knowledge and skills to help develop cutting-edge AI technology?

Frasier's interest is piqued, he ponders the idea for a moment.

Frasier: You know, Roz, that does sound fascinating. The opportunity to work on the forefront of AI advancement, to push the boundaries of what's possible... it's certainly tempting.

Roz: I thought you might say that. And just think, Frasier, you'd be able to help people on a whole new level. AI has the potential to revolutionize so many industries, including mental health.

Frasier: You're right, Roz. With AI, we could create virtual therapists that are available to anyone, anytime. Imagine the impact that could have on people's lives.

Frasier starts to feel a sense of excitement and possibility.

Frasier: I think... I think I need to seriously consider this opportunity. It could be the next chapter in my career, a chance to make a real difference in the world.

Roz smiles, knowing she's struck a chord with Frasier.

Roz: Well, Frasier, I'll get you the contact information for OpenAI. I think it's worth exploring. Who knows, you could be at the forefront of a new era in therapy.

Frasier: Thank you, Roz. I appreciate your support. This could be the beginning of something truly extraordinary.

They exchange a nod of understanding, both excited about the possibilities that lie ahead.

FADE OUT.
3 PDFs exist, no downloading required.
1 or more vectors exist, no embedding required.
```

## Unlimited scraper

`script_scraper` scrapes 3 PDF files and quits. This is because embedding ~10 seasons of PDFs is very expensive.
If you demand more from your FrasierVision, use `script_scraper_unlimited` to scrape all of the scripts.
