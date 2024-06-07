import httpx
from pydantic import BaseModel, Field
from pydantic_core import Url


class MobileXClient(BaseModel):
    base_url: Url = Field(
        default=Url('https://computer-system-team-24.dev.mobilex.kr/api/v1/'),
    )

    def call[To: BaseModel](
        self,
        function: str,
        input: BaseModel,
        output_model: type[To],
    ) -> To | None:
        response = httpx.post(
            url=f'{self.base_url}func/{function}',
            json=input.model_dump(),
            timeout=300.0,
        )
        data = response.json()
        if data is None:
            return None

        return output_model.model_validate(data)
