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

*request*
```json
token create
```
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

*request*
```json
token destroy
```
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

**WRITE PROMPT GENERATE**
</br>

https://catalyst-x226.onrender.com/api/write/generate/

```json
POST api/write/generate/
```
```json
    {
    "style": "poetry",
    "theme": "emotion",
    "category": "relationships and love",
    "sentiment": "harmony",
    "emotion": "joy",
    "prompt_length": "prompt", 
    "user": 1
    }
```
</br>
</br>

**WRITE PROMPT RETRIEVE**
</br>

https://catalyst-x226.onrender.com/api/response/write/id
```json
GET api/response/write/id
```
```json
Retrieves Write instance
```
```json
Retrieves opeanai prompt output
```
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
    "note": null
    }
```
</br>
</br>

**RETRIEVE ALL WRITE PROMPTS**
</br>

https://catalyst-x226.onrender.com/write/prompts/
```json
GET api/write/prompts
```
```json
Retrieves list of user write prompts
```

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
	"note": null
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
	"note": null
	},
    ]
```

**VISUAL ART PROMPT GENERATE**
</br>

https://catalyst-x226.onrender.com/api/visual_art/generate/
```json
POST api/visual_art/generate/
```
```json
    {
    "medium": "painting",
    "theme": "texture",
    "sentiment": "renewal",
    "emotion": "joy",
    "temperature": "0.8",
    "prompt_length": "one word", 
    "user": 1
    }
```

**VISUAL ART PROMPT RETRIEVE**
</br>

https://catalyst-x226.onrender.com/api/response/visual_art/id
```json
GET api/response/visual_art/id
```
```json
Retrieve Visual Art instance
```
```json
Retrieves output/prompt from openai api
```
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
	"note": null
}
```
</br>
</br>

**RETRIEVE ALL VISUAL ART PROMPTS**
</br>

https://catalyst-x226.onrender.com/visual_art/prompts/
```json
GET api/visual_art/prompts
```
```json
Retrieves list of user visual art prompts
```
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
	"note": null
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
	"note": null
	}
    ]
```

**MOVEMENT PROMPT GENERATE**
</br>

https://catalyst-x226.onrender.com/api/movement/generate/

```json
POST api/movement/generate/
```
```json
    {
    "theme": "spatial awareness",
    "somatic": "breath and movement",
    "sentiment": "harmony",
    "emotion": "joy",
    "prompt_length": "one word", 
    "user": 1
    }
```
**MOVEMENT PROMPT RETREIVE**
</br>

https://catalyst-x226.onrender.com/api/response/movement/id
```json
GET api/response/movement/id
```
```json
Retrieve Movement instance
```
```json
Retrieves output/ prompt from openai api
```
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
    "note": null
    }
```
</br>
</br>

**RETRIEVE ALL MOVEMENT PROMPTS**
</br>

https://catalyst-x226.onrender.com/movement/prompts/
```json
GET api/movement/prompts/
```
```json
Retrieve list of user's movement prompts
```
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
	"note": null
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
	"note": null
	}
    ]
```

**MUSIC PROMPT GENERATE**
</br>

https://catalyst-x226.onrender.com/api/music/generate/
```json
POST api/music/generate/
```
```json
    {
    "exploration": "genre fusion",
    "concept": "dynamics",
    "element": "fire",
    "emotion": "courage",
    "length": "prompt",
    "prompt_length": "one word",
    "user": 1
    }
```

**MUSIC PROMPT RETRIEVE**
</br>

https://catalyst-x226.onrender.com/api/response/music/id
```json
GET api/response/music/id
```
```json
Retrieve Music instance
```
```json
Output from openai api
```
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
    "note": null
    }
```
</br>
</br>

**RETRIEVE ALL MUSIC PROMPTS**
</br>

https://catalyst-x226.onrender.com/music/prompts/
```json
GET api/music/prompts/
```
```json
Retrieves list of all user music prompts
```
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
    "note": null
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
    "note": null
    },
]
```
**USER PROMPT ARCHIVE LIST**
</br>

https://catalyst-x226.onrender.com/api/prompt/archive/
```json
GET api/prompt/archive/
```
```
Retrieves list of all user prompts (write, music, visual art, movement)
```

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
        "user": 1
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
	"user": 1
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
	"user": 1
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
        "user": 1
        },
    ]
]
```

**CREATE NOTE**
</br>

https://catalyst-x226.onrender.com/api/note/create/
```json
POST api/note/create/
```

**RETRIEVE NOTE**
</br>

https://catalyst-x226.onrender.com/api/note/id
```json
GET api/note/id
```
```json
Retrieve Note instance
```
```json
    {
    "id": 9,
    "text": "This is a new note"
    }
```
**UPDATE NOTE**
</br>

https://catalyst-x226.onrender.com/api/note/id
```json
PATCH api/note/id
```

**DELETE NOTE**
</br>

https://catalyst-x226.onrender.com/note/id
```json
DESTROY api/note/id
```


**WELCOME PROMPT GENERATE**
</br>

https://catalyst-x226.onrender.com/api/welcome/generate/
```json
POST api/welcome/generate/
```

**RETRIEVE WELCOME PROMPT**
</br>

https://catalyst-x226.onrender.com/api/welcome/id
```json
GET api/welcome/id
```
```json
Retrieve Welcome instance
```
```json
    {
    "id": 3,
    "output_text": "Welcome to the app! How can I assist you today?"
    }
```
