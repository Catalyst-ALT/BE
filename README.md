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
> https://catalyst-x226.onrender.com/auth/users/

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
    // "id": 1
    }
```
</br>
</br>

**LOGIN**
> https://catalyst-x226.onrender.com/auth/token/login/

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
> https://catalyst-x226.onrender.com/auth/token/logout/

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
> https://catalyst-x226.onrender.com/api/profile/username/

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

**POEM PROMPT GENERATE POST**
> https://catalyst-x226.onrender.com/api/poem/generate/

*request*
```json
POST api/poem/generate/
```
```json
    {
	"theme": "emotion",
	"category": "relationships and love",
	"sentiment": "harmony",
	"emotion": "joy",
	"input_sentiment": null,
	"input_emotion": null,
	"user": 1
    }
```
*response*
```json
    {
	"id": 12,
	"theme": "emotion",
	"category": "relationships and love",
	"sentiment": "harmony",
	"emotion": "joy",
	"input_sentiment": null,
	"input_emotion": null,
	"user": 1
    }
```
</br>
</br>

**POEM PROMPT GENERATE GET**
> https://catalyst-x226.onrender.com/api/response/poem/id
```json
Output from openai api
```

```json
GET api/response/poem/<id>
```
*response*
```json
    {
	"id": 45,
	"theme": "exploration",
	"category": "advocacy",
	"sentiment": "resilience",
	"emotion": "grief",
	"input_sentiment": null,
	"input_emotion": null,
	"output": "Uncharted horizons etch the undeniable path of your journey, as you champion for voices and navigate turmoil of crossed skies; poetry unfolds within your steadfast pilgrimage of sorrow and renewal.",
	"user": 1
    }
```
**VISUAL ART PROMPT GENERATE POST**
> https://catalyst-x226.onrender.com/api/visual_art/generate/
```json
POST api/visual_art/generate/
```
```json
    {
	"medium": "painting",
	"theme": "texture",
	"sentiment": "renewal",
	"emotion": "joy",
	"temperature": 1.0,
	"user": 1, 
	"output": ""
    }
```



**VISUAL ART PROMPT GENERATE GET**
> https://catalyst-x226.onrender.com/api/response/visual_art/id
```json
Output from openai api
```

```json
GET api/response/visual_art/id
```
```json
    {
	"id": 25,
	"medium": "painting",
	"theme": "texture",
	"sentiment": "renewal",
	"emotion": "joy",
	"temperature": 1,
	"output": "Create a vibrant masterpiece capturing the essence of transformation and delight, where layered brushstrokes evoke both tactile and emotional sensations.",
	"user": 1
    }
```