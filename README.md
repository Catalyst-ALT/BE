# Catalyst BE ReadME 


https://catalyst-x226.onrender.com


**Token Authentication System**
* Djoser
* Docs: https://djoser.readthedocs.io/en/latest/introduction.html
  
**Deployment**
* Render
* Database: Postgresql@14
* Docs: https://render.com/docs/deploy-django
</br>
</br>


**CREATE USER**
</br>

https://catalyst-x226.onrender.com/auth/users/

*request*
```json
POST  auth/users/
```
```json
    {
    "username": "superuser",
    "password": "somepassword"
    }
```

*response*
```json
HTTP_201_created
```
```json
    {
    "username": "superuser",
    "password": "somepassword",
    }
```
</br>
</br>

**LOGIN**
</br>

https://catalyst-x226.onrender.com/auth/token/login/


**Token Create**

*request*
```json
POST auth/token/login/
```
```json
    {
    "username": "superuser",
    "password": "somepassword"
    }
```

*response*
```json
HTTP_200_OK
```
```json
    {
    "auth_token": "somereallylonglistofnumbersandletters"
    }
```
</br>
</br>


**LOGOUT**
</br>

https://catalyst-x226.onrender.com/auth/token/logout/

**Token Destroy**

*request*

```json
POST auth/token/logout/
```

*response*
```json
HTTP_204_NO_CONTENT
```

</br>
</br>

**PROFILE**
</br>

https://catalyst-x226.onrender.com/api/profile/username/

*request*
```json
GET api/profile/<username>/
```

*response*
```json
    {
    "username": "superuser",
    }
```
*request*
```json
PATCH  api/profile/<username>/
```

*response*
```json
    {
    "username": "superuser"
    },
```

*request*
```json
DELETE  api/profile/<username>/
```

*response*
```json
HTTP_204_NO_CONTENT
```

</br>
</br>

**WRITE INSTANCE CREATE**
</br>

https://catalyst-x226.onrender.com/api/write/generate/

```json
POST api/write/generate/
```
**Purpose:**
* Creates Write instance
* Generates opeanai **prompt output**
* Sends info to DB for **call to openai**
* Creates a **note** associated with this instance with empty string as default 
* Creates an **id** for this instance
* Auto adds **'created_at'** date/time
* Adds field 'input_length' for call to api


```json
    {
    "style": "poetry",
    "theme": "emotion",
    "category": "relationships and love",
    "sentiment": "harmony",
    "emotion": "joy",
    "prompt_length": "prompt",
    }
```
*Required Fields: 'style', 'theme', 'category', 'sentiment', 'emotion', 'prompt_length'*

</br>
</br>

**WRITE SINGLE INSTANCE RETRIEVE**
</br>

https://catalyst-x226.onrender.com/api/response/write/id
```json
GET api/response/write/id
```
**Purpose:**
* Retrieves single Write instance
* Retrieves the **id** for this instance
* Retrieves the **note** associated with this instance
* Retrieves from DB opeanai prompt **output**
* Retrieves **'created_at'** date/time for this instance

```json
    {
    "id": 104,
    "style": "poetry",
    "theme": "emotion",
    "category": "relationships and love",
    "sentiment": "harmony",
    "emotion": "joy",
    "prompt_length": "prompt",
    "input_length": "Let the prompt be 20-25 words",
    "output": "Write a story about two souls who find solace in each other's presence, navigating the complexities of their emotions and forging a bond that radiates harmony, joy, and profound love.",
    "created_at": "2023-07-19T21:49:42.927227Z",
    "user": 1,
    "note": ""
    }
```
*New Fields: 'id', 'input_length', 'output', 'user', 'note', 'created_at'*
</br>
</br>

**WRITE INSTANCE UPDATE**
</br>
https://catalyst-x226.onrender.com/api/response/write/id
```json
PATCH api/response/write/id
```

**Purpose**
* Allows user to **update their note** associated with this instance
</br>
</br>

**RETRIEVE ALL WRITE INSTANCES**
</br>

https://catalyst-x226.onrender.com/write/
```json
GET api/write/
```
**Purpose**
* Retrieves **list** of user Write instances
* Retrieves all openai **outputs** for the collection of user Write instances
* Retrieves all **notes** for the collection of user Write instances

```json
    [
	{
	"id": 67,
	"style": "creative writing",
	"theme": "nature",
	"category": "relationships and love",
	"sentiment": "harmony",
	"emotion": "joy",
	"prompt_length": "prompt",
	"input_length": "Let the prompt be 20-25 words",
	"output": "",
	"created_at": "2022-08-07T00:00:00Z",
	"user": 1,
	"note": ""
	},
	{
	"id": 80,
	"style": "poetry",
	"theme": "emotion",
	"category": "relationships and love",
	"sentiment": "harmony",
	"emotion": "joy",
	"prompt_length": "prompt",
	"input_length": "Let the prompt be 20-25 words",
	"output": "Explore the captivating tale of two souls intertwined, braving the trials of life together, where profound connections overcome all obstacles, paving the way for boundless euphoria.",
	"created_at": "2023-07-19T00:48:55.149209Z",
	"user": 1,
	"note": ""
	},
    ]
```
</br>
</br>

**VISUAL ART INSTANCE CREATE**
</br>

https://catalyst-x226.onrender.com/api/visual_art/generate/
```json
POST api/visual_art/generate/
```
**Purpose:**
* Creates VisualArt Instance
* Generates opeanai **prompt output**
* Sends info to DB for **call to openai**
* Creates a **note** associated with this instance with empty string as default 
* Creates an **id** for this instance
* Auto adds **'created_at'** date/time
* Adds 'input_length" for call to api

```json
    {
    "medium": "painting",
    "theme": "texture",
    "sentiment": "renewal",
    "emotion": "joy",
    "prompt_length": "one word", 
    }
```
*Required Fields: 'medium', 'theme', 'sentiment', 'emotion', 'prompt_length'*
</br>
</br>

**VISUAL ART SINGLE INSTANCE RETRIEVE**
</br>

https://catalyst-x226.onrender.com/api/response/visual_art/id
```json
GET api/response/visual_art/id
```
**Purpose:**
* Retrieves single VisualArt instance
* Retrieves the **id** for this instance
* Retrieves the **note** associated with this instance
* Retrieves opeanai prompt **output**
* Retrieves **'created_at'** date/time for this instance
```json
    {
	"id": 70,
	"medium": "painting",
	"theme": "texture",
	"sentiment": "renewal",
	"emotion": "joy",
	"prompt_length": "one word",
	"input_length": "Let the prompt be only 1 word",
	"output": "Burst",
	"created_at": "2023-07-19T21:59:42.298361Z",
	"user": 1,
	"note": ""
}
```
*New Fields: 'id', 'input_length', 'output', 'user', 'note', 'created_at'*
</br>
</br>

**VISUAL ART INSTANCE UPDATE**
</br>
https://catalyst-x226.onrender.com/api/response/visual_art/id
```json
PATCH api/response/visual_art/id
```

**Purpose**
* Allows user to **update their note** associated with this instance
</br>
</br>

**RETRIEVE ALL VISUAL ART INSTANCES**
</br>

https://catalyst-x226.onrender.com/visual_art/
```json
GET api/visual_art/
```
**Purpose**
* Retrieves **list** of user Visual Art instances
* Retrieves all openai **outputs** for the collection of user Visual Art instances
* Retrieves all **notes** for the collection of user Visual Art instances
```json
    ]
        {
	"id": 69,
	"medium": "painting",
	"theme": "texture",
	"sentiment": "renewal",
	"emotion": "joy",
	"prompt_length": "prompt",
	"input_length": "Let the prompt be 20-25 words",
	"output": "Create a vibrant masterpiece that captures the essence of growth and happiness through the interplay of various tactile elements.",
	"created_at": "2023-07-19T21:59:29.054715Z",
	"user": 1,
	"note": ""
	},
	{
	"id": 70,
	"medium": "painting",
	"theme": "texture",
	"sentiment": "renewal",
	"emotion": "joy",
	"prompt_length": "one word",
	"input_length": "Let the prompt be only 1 word",
	"output": "Burst",
	"created_at": "2023-07-19T21:59:42.298361Z",
	"user": 1,
	"note": ""
	}
    ]
```
</br>
</br>

**MOVEMENT INSTANCE CREATE**
</br>

https://catalyst-x226.onrender.com/api/movement/generate/

```json
POST api/movement/generate/
```
**Purpose:**
* Creates Movement instance
* Generates opeanai **prompt output**
* Sends info to DB for **call to openai**
* Creates a **note** associated with this instance with empty string as default 
* Creates an **id** for this instance
* Auto adds **'created_at'** date/time
* Adds 'input_length" for call to api

```json
    {
    "theme": "spatial awareness",
    "somatic": "breath and movement",
    "sentiment": "harmony",
    "emotion": "joy",
    "prompt_length": "one word",
    }
```
*Required Fields: 'theme', 'somatic', 'emotion', 'prompt_length'*
</br>
</br>

**MOVEMENT SINGLE INSTANCE RETREIVE**
</br>

https://catalyst-x226.onrender.com/api/response/movement/id
```json
GET api/response/movement/id
```
**Purpose:**
* Retrieves single Movement instance
* Retrieves the **id** for this instance
* Retrieves the **note** associated with this instance
* Retrieves opeanai prompt **output**
* Retrieves **'created_at'** date/time for this instance
```json
    {
    "id": 9,
    "theme": "spatial awareness",
    "somatic": "breath and movement",
    "sentiment": "harmony",
    "emotion": "joy",
    "prompt_length": "one word",
    "input_length": "Let the prompt be only 1 word",
    "output": "Flow",
    "created_at": "2023-07-19T22:02:43.640107Z",
    "user": 1,
    "note": ""
    }
```
*New Fields: 'id', 'input_length', 'output', 'user', 'note', 'created_at'*
</br>
</br>

**MOVEMENT INSTANCE UPDATE**
</br>
https://catalyst-x226.onrender.com/api/response/movement/id
```json
PATCH api/response/movement/id
```

**Purpose**
* Allows user to **update their note** associated with this instance
</br>
</br>

**RETRIEVE ALL MOVEMENT INSTANCES**
</br>

https://catalyst-x226.onrender.com/movement/
```json
GET api/movement/
```
**Purpose**
* Retrieves **list** of user Movement instances
* Retrieves all openai **outputs** for the collection of user Write instances
* Retrieves all **notes** for the collection of user Write instances
```json
    [
        {
	"id": 8,
	"theme": "spatial awareness",
	"somatic": "breath and movement",
	"sentiment": "harmony",
	"emotion": "joy",
	"prompt_length": "prompt",
	"input_length": "Let the prompt be 20-25 words",
	"output": "Explore the limitless expanse within, unleashing a symphony of fluidity and grace, as you dance with boundless delight, embracing the interconnectedness of body and space.",
	"created_at": "2023-07-19T22:02:15.049638Z",
	"user": 1,
	"note": ""
	},
	{
	"id": 9,
	"theme": "spatial awareness",
	"somatic": "breath and movement",
	"sentiment": "harmony",
	"emotion": "joy",
	"prompt_length": "one word",
	"input_length": "Let the prompt be only 1 word",
	"output": "Flow",
	"created_at": "2023-07-19T22:02:43.640107Z",
	"user": 1,
	"note": ""
	}
    ]
```
</br>
</br>

**MUSIC CREATE INSTANCE**
</br>

https://catalyst-x226.onrender.com/api/music/generate/
```json
POST api/music/generate/
```
**Purpose:**
* Create Music instance
* Generates opeanai **prompt output**
* Sends info to DB for **call to openai**
* Creates a **note** associated with this instance with empty string as default 
* Creates an **id** for this instance
* Auto adds **'created_at'** date/time
* Adds 'input_length" for call to api
```json
    {
    "exploration": "genre fusion",
    "concept": "dynamics",
    "element": "fire",
    "emotion": "courage",
    "prompt_length": "one word",
    }
```
*Required Fields: 'exploration', 'concept', 'emotion', 'element', 'prompt_length'*
</br>
</br>

**MUSIC SINGLE INSTANCE RETRIEVE**
</br>

https://catalyst-x226.onrender.com/api/response/music/id
```json
GET api/response/music/id
```
**Purpose:**
* Retrieves a single Music instance
* Retrieves the **id** for this instance
* Retrieves the **note** associated with this instance
* Retrieves opeanai prompt **output**
* Retrieves **'created_at'** date/time for this instance
```json
    {
    "id": 30,
    "exploration": "genre fusion",
    "concept": "dynamics",
    "element": "fire",
    "emotion": "courage",
    "prompt_length": "one word",
    "input_length": "Let the prompt be only 1 word",
    "output": "Ignite",
    "created_at": "2023-07-19T22:04:30.480555Z",
    "user": 1,
    "note": ""
    }
```
*New Fields: 'id', 'input_length', 'output', 'user'(user_id), 'note', 'created_at'*
</br>
</br>

**MUSIC INSTANCE UPDATE**
</br>
https://catalyst-x226.onrender.com/api/response/music/id
```json
PATCH api/response/music/id
```

**Purpose**
* Allows user to **update their note** associated with this instance
</br>
</br>

**RETRIEVE ALL MUSIC INSTANCES**
</br>

https://catalyst-x226.onrender.com/music/
```json
GET api/music/
```
**Purpose**
* Retrieves **list** of user Music instances
* Retrieves all openai **outputs** for the collection of user Music instances
* Retrieves all **notes** for the collection of user Music instances
```json
[
    {
    "id": 34,
    "exploration": "genre fusion",
    "concept": "dynamics",
    "element": "fire",
    "emotion": "courage",
    "prompt_length": "prompt",
    "input_length": "Let the prompt be 20-25 words",
    "output": "Create an electrifying sonic journey that seamlessly blends diverse genres, igniting the listener's spirit with bold dynamics and invoking a sense of fearless passion.",
    "created_at": "2023-07-19T22:08:35.122715Z",
    "user": 1,
    "note": "Art is life"
    },
    {
    "id": 29,
    "exploration": "genre fusion",
    "concept": "dynamics",
    "element": "fire",
    "emotion": "courage",
    "prompt_length": "one word",
    "input_length": "Let the prompt be only 1 word",
    "output": "Ignite",
    "created_at": "2023-08-07T00:00:00Z",
    "user": 1,
    "note": "I love this app"
    },
]
```
</br>
</br>

**FOLIOS**
</br>

https://catalyst-x226.onrender.com/api/folios/
```json
GET api/folios/
```
**Purpose**
* Retrieves **list** of all instances (Write, Music, VisualArt, Movement) associated with user
* Retrieves list of **notes** associated with user (Write notes, Music notes, VisualArt notes, Movement notes), **including any notes the user has updated**
* Retrieves **list** of all openai api **prompt outputs** (Write output, Music output, VisualArt output, Movement output)

```json
[
    {
    "username": "superuser",
    }
    "music": [
        {
        "id": 2,
        "exploration": "musical time travel",
        "concept": "tempo",
        "element": "fire",
        "emotion": "joy",
	"prompt_length": "prompt",
	"input_length": "Let the prompt be 20-25 words",
	"output": "Journey through melodic epochs fuelled by celebratory rhythms, kindling a passionate storm. Create harmonies that transport listeners through a timeless musical dimension.",
        "user": 1,
        "note": ""
	},
    ],
    "visual_arts": [
	{
	"id": 25,
	"medium": "painting",
	"theme": "texture",
	"sentiment": "renewal",
	"emotion": "joy",
	"prompt_length": "prompt",
	"input_length": "Let the prompt be 20-25 words",
	"output": "Create a vibrant masterpiece capturing the essence of transformation and delight, where layered brushstrokes evoke both tactile and emotional sensations.",
	"user": 1,
    "note": "", 
	},
    ],
    "movements": [
	{
	"id": 5,
	"theme": "spatial awareness",
	"somatic": "breath and movement",
	"sentiment": "harmony",
	"emotion": "joy",
	"prompt_length": "prompt",
	"input_length": "Let the prompt be 20-25 words",
	"output": "Create a dynamic dance piece that explores the seamless interplay of bodies in space, flowing breath, and expressive movements, evoking a sense of pure and radiant bliss.",
	"user": 1,
    "note": ""
        },	
    ],
    "writes": [
	{
        "id": 66,
        "style": "word play",
        "theme": "emotion",
        "category": "relationships and love",
        "sentiment": "renewal",
        "emotion": "joy",
        "prompt_length": "one word",
        "input_length": "Let the prompt be only 1 word",
        "output": "Spark",
        "user": 1,
        "note": ""
        },
    ]
]
```


**WELCOME PROMPT GENERATE**
</br>

https://catalyst-x226.onrender.com/api/welcome/generate/
```json
POST api/welcome/generate/
```

**Purpose:**
* Triggers call to openai's api to generate welcome message

*Required Fields: none"*

</br>
</br>

**RETRIEVE WELCOME MESSAGE**
</br>

https://catalyst-x226.onrender.com/api/welcome/id
```json
GET api/welcome/id
```
**Purpose:**
* Retrieves welcome output/message from DB
```json
    {
    "id": 3,
    "output_text": "Welcome to the app! How can I assist you today?"
    }
```
*New Fields: 'id', 'output_text"*
</br>
</br>


**DEFINITION GENERATE**
</br>
https://catalyst-x226.onrender.com/api/definition/generate/
```json
POST api/definition/generate/
```

**Purpose:**
* Sends word (to be defined) to DB for call to openai's api

```json
    {
    "word": "gracious"
    }
```
*Required Field: "word"*
</br>
</br>

**RETRIEVE DEFINITION**
</br>

https://catalyst-x226.onrender.com/api/definition/id
```json
GET api/definition/id
```

**Purpose**
* Retrieves output/definition from DB

```json
    {
    "id": 7,
    "word": "gracious",
    "definition": "Gracious means being kind, polite, and showing good manners towards others. It is when someone behaves in a considerate and generous way, making others feel valued and respected."
    }
```
*New Fields: 'id', 'definition'*
</br>
</br>

**USER NOTEBOOK (ALL PROMPTS W/ NOTES)**
</br>
https://catalyst-x226.onrender.com/api/notebook/
```json
GET api/notebook/
```
**Purpose**

* Filters for the prompts the user has written notes on 
* Retrieves a list
  
```json
    {
    "id": 104,
    "user": 1,
    "style": "poetry",
    "theme": "emotion",
    "category": "relationships and love",
    "sentiment": "harmony",
    "emotion": "joy",
    "prompt_length": "prompt",
    "input_length": "Let the prompt be 20-25 words",
    "created_at": "2023-07-19T21:49:42.927227Z",
    "output": "Write a story about two souls who find solace in each other's presence, navigating the complexities of their emotions and forgin
    a bond that radiates harmony, joy, and profound love.",
    "note": "take notes",
    "save": null
    },
```

**USER SAVED PROMPTS**
</br>
https://catalyst-x226.onrender.com/api/prompts/saved/
```json
GET api/prompts/saved/
```


**USER UPLOAD FILE (IMAGE, ETC.)**
</br>
https://catalyst-x226.onrender.com/api/upload/create/
```json
POST api/upload/create/
```

**Purpose**
* For user to upload files (images, videos, etc) to app

</br>
</br>

**GET SINGLE USER FILE UPLOAD (IMAGE, ETC.)**
</br>
https://catalyst-x226.onrender.com/api/upload/id
```json
GET api/uploads/id
```

**Purpose**
* To retrieve and display a single file the user has uploaded (for example an image to be diplayed in the folios section)
  
</br>
</br>

**GET A LIST OF USER FILE UPLOADS**
</br>
https://catalyst-x226.onrender.com/api/uploads/
```json
GET api/uploads/
```

**Purpose**
* To retrieve and display a list of files the user had uploaded (for example a list of images to be displayed in the folios section)





