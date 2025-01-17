from typing import List
from fastapi import APIRouter, Body, Depends, HTTPException, Query

from database import get_db_session
from users.auth.deps import get_user
from users.etudiants.schemas import CreateEtudiantSchema
from .presenter import  ThesisPresenter
<<<<<<< HEAD
from .schemas import CreateThesisSchema
from sqlalchemy.ext.asyncio import AsyncSession
from .deps import response_data, get_user, get_presenter, \
=======
from .schemas import CreateThesisSchema, UpdateThesisSchema
from sqlalchemy.ext.asyncio import AsyncSession
from .deps import get_limit_offset_thesis, response_data, get_user, get_presenter, \
>>>>>>> 72a4943caa0a8fe86e91703bd7adad3a3e137997
    get_slug_user, get_thesis_user, get_limit_offset_user, \
    get_create_data_user, get_updated_data_slug_user

thesis_controllers = APIRouter(prefix='/thesis', tags=['thesis'])


<<<<<<< HEAD
=======
@thesis_controllers.get(**response_data.get('all_thesis'))
async def get_all_thesis(
        annee_id: int,
        presenter: ThesisPresenter = Depends(get_presenter),
        limit: int | None = 20,
        offset: int | None = 0
):
    data: dict = await get_limit_offset_thesis(limit, offset, annee_id)
    return await presenter.get_all_thesis(**data)


@thesis_controllers.get(**response_data.get('thesis'))
async def get_thesis(
    years_id: int,
    user=Depends(get_user),
    presenter: ThesisPresenter = Depends(get_presenter)
    
):
    # data: dict = await get_limit_offset_user(user.id, years_id)
    return await presenter.get_thesis(utilisateur_id=user.id, years_id=years_id)

>>>>>>> 72a4943caa0a8fe86e91703bd7adad3a3e137997
@thesis_controllers.post(**response_data.get('create_thesis'))
async def create_thesis(
        thesis_data: CreateThesisSchema,
        matricules: str,  # Les matricules sont envoyés en tant que chaîne, séparés par des virgules
<<<<<<< HEAD
=======
        user=Depends(get_user),
>>>>>>> 72a4943caa0a8fe86e91703bd7adad3a3e137997
        presenter: ThesisPresenter = Depends(get_presenter),
        db: AsyncSession = Depends(get_db_session)
    ):
    try:
        matricules_list = [m.strip() for m in matricules.split(',')]
<<<<<<< HEAD
        thesis_id = await presenter.create_thesis(thesis_data, matricules_list, db)
        return {"thesis_id": thesis_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))




# async def create_thesis(
#     thesis_data: CreateThesisSchema,
#     user=Depends(get_user),
#     presenter: ThesisPresenter = Depends(get_presenter),
#     db: AsyncSession = Depends(get_db_session)
# ):
#     return await presenter.create_thesis(thesis_data, db)
=======
        thesis_id = await presenter.create_thesis(user.id, thesis_data, matricules_list, db)
        return {"thesis_id": thesis_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@thesis_controllers.patch(**response_data.get('update_thesis'))
async def update_thesis(
        updated_data: UpdateThesisSchema,
        thesis_slug: str, user=Depends(get_user),
        presenter: ThesisPresenter = Depends(get_presenter),
):
    data: dict = await get_updated_data_slug_user(
        updated_data, thesis_slug, user.id)
    return await presenter.update_thesis(**data)

@thesis_controllers.get(**response_data.get('thesisa'))
async def get_thesisa(
        thesis_slug: str,
        presenter: ThesisPresenter = Depends(get_presenter),
):
    return await presenter.get_thesisa(thesis_slug=thesis_slug)


# @thesis_controllers.get(**response_data.get('memorant'))
# async def get_student_ids_for_thesis(
#     annee_id: int,
#     presenter: ThesisPresenter = Depends(get_presenter),
#     limit: int = 20,
#     offset: int = 0
# ):
#     try:
#         data = await get_limit_offset_thesis(limit, offset, annee_id)
#         theses = await presenter.get_all_thesis(**data)
        
#         # Extracting etudiant_ids from theses
#         etudiant_ids = []
#         for thesis in theses:
#             etudiant_ids.extend(thesis['etudiant_id'])
        
#         return {
#             'etudiant_ids': etudiant_ids
#         }
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

@thesis_controllers.get(**response_data.get('memorant'))
async def get_all_thesis_with_students(
        annee_id: int,
        presenter: ThesisPresenter = Depends(get_presenter),
        limit: int | None = 20,
        offset: int | None = 0,
        db: AsyncSession = Depends(get_db_session)
):
    print(f"Controller: annee_id={annee_id}, limit={limit}, offset={offset}")
    try:
        theses_with_students = await presenter.get_all_thesis_with_students(annee_id, limit, offset, db)
        return {'theses_with_students': theses_with_students}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
>>>>>>> 72a4943caa0a8fe86e91703bd7adad3a3e137997
