import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ProductsListComponent } from './products-list/products-list.component';
import { CategoriesComponent } from './categories/categories.component';
import { AppComponent } from './app.component';


const routes: Routes = [
  {
    path: '', component: AppComponent
  },
  {
    path: 'categories', redirectTo: '', pathMatch: 'full'
  },
  {
    path: 'categories/:categoryId', component: ProductsListComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
