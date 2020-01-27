#!groovy                                                                           

properties(                                                                        
    [                                                                              
        [                                                                          
            $class: 'jenkins.model.BuildDiscarderProperty', strategy: [$class: 'LogRotator', numToKeepStr: '10', artifactNumToKeepStr: '10'],
            $class: 'CopyArtifactPermissionProperty', projectNames: '*'            
        ]                                                                          
    ]                                                                              
)   

def prepareEnv() {                                                                 
    unstash 'binaries'                                                             
                                                                                   
    env.WORKSPACE = pwd()                                                          
                                                                                   
    sh "find ${env.WORKSPACE}"                                                     
                                                                                   
    sh 'mkdir -p SPECS SOURCES'                                                    
    sh "cp dist/*.zip SOURCES/upsilon-drone-probes.zip"                      
}                                                                                 

def buildRpm(dist) {                                                               
    deleteDir()                                                                    

	prepareEnv()
                                                                                                                                                                      
    sh 'unzip -jo SOURCES/upsilon-drone-probes.zip "upsilon-drone-probes/var/pkg/upsilon-drone-probes.spec" "upsilon-drone-probes/.buildid.rpmmacro" -d SPECS/'
    sh "find ${env.WORKSPACE}"                                                     
                                                                                   
    sh "rpmbuild -ba SPECS/upsilon-drone-probes.spec --define '_topdir ${env.WORKSPACE}' --define 'dist ${dist}'"
                                                                                   
    archive 'RPMS/noarch/*.rpm'                                                    
}                    

node {
	stage "Build"

	deleteDir()
	checkout scm

	sh './make.sh'

	stash includes: 'dist/*.zip', name: 'binaries'
}

stage "Package"

node {                                                                             
    buildRpm("el7")                                                                
}                                                                                  
                                                                                   
node {                                                                             
    buildRpm("el6")                                                                
}                                                                                  
                                                                                   
node {                                                                             
    buildRpm("fc24")                                                               
}


