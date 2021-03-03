#![allow(non_snake_case)]

use std::{any::{Any, TypeId}, cell::UnsafeCell, collections::HashMap};

use anymap::AnyMap;
struct Entity{
	id:usize
}
trait Component{
	fn update(&self);
}
struct EngineContext {
	engine: UnsafeCell<Engine>
}

struct BoundingBox {
} 
struct CameraFollow {
}
impl Component for BoundingBox {
	fn update(&self) {
		println!("Bounding Box");
	}
}
impl Component for CameraFollow {
	fn update(&self) {
		println!("Camera follow");
	}
}
struct VecStorage<T> {
	data: Vec<T>
}
impl<'a, T> VecStorage<T>{
	fn new()->Self {
		Self{
			data: Vec::new()
		}
	}
	fn add(&mut self,ent: &Entity,comp: T){
		self.data.push(comp);
	}
	fn get(&'a self,ent: usize)->&'a T{
		&self.data[ent]
	} 
}

struct Engine {
	componentLists: HashMap<TypeId, Box< dyn Any >>,
}
impl<'a> Engine {
	fn new()->Self {
		Self{
			componentLists:HashMap::new(),
		}
	}
	fn registerComponent<T : Component + 'static>(&mut self){
		let typeId=TypeId::of::<T>();
		self.componentLists.insert(typeId,Box::new(VecStorage::<T>::new()));
	}
	fn addComponent<T: Component + 'static>(&mut self,ent: &Entity, comp: T) {

		let typeId=TypeId::of::<T>();
		let compList=self.componentLists.get_mut(&typeId).unwrap().downcast_mut::<VecStorage<T>>().unwrap();
		
		compList.add(ent,comp);
	}
	fn getComponent<T:Component + 'static>(&self,ent: usize)-> &T{
		let typeId =TypeId::of::<T>();
		let compList=self.componentLists[&typeId].downcast_ref::<VecStorage<T>>().unwrap();

		compList.get(ent)
	}
}
impl EngineContext {
	fn new()->Self{
		Self{
			engine: UnsafeCell::new(Engine::new())
		}
	}
}
fn create() {
	//createComponent!(BoundingBox);

}
fn update() {
	//updateComponent!();
}
fn main(){
	let mut engine = Engine::new();
	engine.registerComponent::<BoundingBox>();
	engine.registerComponent::<CameraFollow>();

	let dummy=Entity{
		id:1
	};
	engine.addComponent(&dummy, BoundingBox{});
	engine.addComponent(&dummy, CameraFollow{});

	engine.getComponent::<BoundingBox>(0).update();
	engine.getComponent::<CameraFollow>(0).update();
}
