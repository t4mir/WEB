import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LoginpageComponent } from './loginpage/loginpage.component';
import { CompaniesComponent } from './companies/companies.component';
import { CategoriesComponent } from './categories/categories.component';
import { ProductsListComponent } from './products-list/products-list.component';
import { GamesallComponent } from './gamesall/gamesall.component';

const routes: Routes = [
  {
    path: '',  redirectTo: 'login', pathMatch: 'full'
  },
  {
    path: 'login', component: LoginpageComponent
  },
  {
    path: 'api/companies', component: CompaniesComponent
  },
  {
    path: 'api/categories', component: CategoriesComponent
  },
  {
    path: 'api/categories/:id', component: ProductsListComponent
  },
  {
    path: 'api/companies/:id', component: CompaniesComponent  
  },
  {
    path: 'api/games', component: GamesallComponent
  },
  {
    path: 'api/games/:id', component: GamesallComponent
  },
  {
    path: 'users', component: CompaniesComponent
  }
]



@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
